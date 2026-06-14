import * as vscode from 'vscode';
import * as child_process from 'child_process';
import * as path from 'path';
import { findFreePort, fileToServerPath, httpGet } from './utils';

export type ServerState = 'stopped' | 'starting' | 'running';

/**
 * PHP内置服务器管理器（单例）
 * 管理 PHP -S 的生命周期：启动、停止、重启
 */
export class PhpServerManager {
    private static instance: PhpServerManager;

    private phpProcess: child_process.ChildProcess | null = null;
    private port: number | null = null;
    private host: string = '127.0.0.1';
    private state: ServerState = 'stopped';

    private _onStateChange = new vscode.EventEmitter<ServerState>();
    readonly onStateChange: vscode.Event<ServerState> = this._onStateChange.event;

    private constructor() {}

    static getInstance(): PhpServerManager {
        if (!PhpServerManager.instance) {
            PhpServerManager.instance = new PhpServerManager();
        }
        return PhpServerManager.instance;
    }

    getState(): ServerState {
        return this.state;
    }

    getPort(): number | null {
        return this.port;
    }

    getUrl(): string | null {
        if (!this.port) return null;
        return `http://${this.host}:${this.port}`;
    }

    isRunning(): boolean {
        return this.state === 'running';
    }

    /**
     * 启动PHP内置服务器
     * 返回实际使用的端口号
     */
    async start(): Promise<number> {
        if (this.state === 'starting') {
            throw new Error('服务器正在启动中...');
        }
        if (this.state === 'running' && this.phpProcess) {
            return this.port!;
        }

        const config = vscode.workspace.getConfiguration('phpBrowser');
        const phpPath = config.get<string>('phpPath', 'D:/php/php-8.5.1-Win32-vs17-x64/php');
        const preferredPort = config.get<number>('port', 8765);
        this.host = config.get<string>('host', '127.0.0.1');

        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders || workspaceFolders.length === 0) {
            throw new Error('请先打开一个工作区文件夹');
        }
        const docRoot = workspaceFolders[0].uri.fsPath;

        // 检查PHP可执行文件
        const phpExists = await this.checkPhpExists(phpPath);
        if (!phpExists) {
            const action = await vscode.window.showErrorMessage(
                `找不到PHP可执行文件: ${phpPath}`,
                '打开设置'
            );
            if (action === '打开设置') {
                vscode.commands.executeCommand(
                    'workbench.action.openSettings',
                    'phpBrowser.phpPath'
                );
            }
            throw new Error(`PHP可执行文件不存在: ${phpPath}`);
        }

        // 查找空闲端口
        let port: number;
        try {
            port = await findFreePort(preferredPort);
        } catch (err) {
            throw new Error(`无法分配端口: ${err}`);
        }

        this.state = 'starting';
        this._onStateChange.fire(this.state);

        return new Promise<number>((resolve, reject) => {
            try {
                const phpProcess = child_process.spawn(
                    phpPath,
                    ['-S', `${this.host}:${port}`, '-t', docRoot],
                    {
                        cwd: docRoot,
                        windowsHide: true,
                        stdio: ['ignore', 'pipe', 'pipe'],
                    }
                );

                let started = false;

                phpProcess.stdout?.on('data', (data: Buffer) => {
                    console.log(`[PHP Server stdout] ${data.toString()}`);
                });

                phpProcess.stderr?.on('data', (data: Buffer) => {
                    const msg = data.toString();
                    console.log(`[PHP Server stderr] ${msg}`);

                    // PHP内置服务器的启动信息输出在stderr
                    if (!started && msg.includes('started')) {
                        started = true;
                    }
                });

                phpProcess.on('error', (err) => {
                    console.error(`[PHP Server] 启动错误:`, err);
                    this.phpProcess = null;
                    this.state = 'stopped';
                    this._onStateChange.fire('stopped');
                    reject(new Error(`PHP服务器启动失败: ${err.message}`));
                });

                phpProcess.on('exit', (code) => {
                    console.log(`[PHP Server] 进程退出，退出码: ${code}`);
                    this.phpProcess = null;
                    if (this.state !== 'stopped') {
                        this.state = 'stopped';
                        this._onStateChange.fire('stopped');
                    }
                });

                this.phpProcess = phpProcess;
                this.port = port;

                // 等待服务器就绪
                this.waitForServer(port, 3000)
                    .then(() => {
                        started = true;
                        this.state = 'running';
                        this._onStateChange.fire('running');
                        resolve(port);
                    })
                    .catch(() => {
                        // 即使轮询超时，也可能只是慢启动
                        // 标记为运行，用户使用时若不可用会看到浏览器错误页
                        this.state = 'running';
                        this._onStateChange.fire('running');
                        resolve(port);
                    });
            } catch (err) {
                this.state = 'stopped';
                this._onStateChange.fire('stopped');
                reject(err);
            }
        });
    }

    /**
     * 停止PHP服务器
     */
    stop(): void {
        if (!this.phpProcess) {
            this.state = 'stopped';
            this._onStateChange.fire('stopped');
            return;
        }

        const pid = this.phpProcess.pid;
        if (pid) {
            try {
                child_process.execSync(
                    `taskkill /F /T /PID ${pid}`,
                    { windowsHide: true }
                );
            } catch (err) {
                // 进程可能已经结束
                console.warn(`[PHP Server] taskkill 警告: ${err}`);
            }
        }

        this.phpProcess = null;
        this.port = null;
        this.state = 'stopped';
        this._onStateChange.fire('stopped');
    }

    /**
     * 重启服务器
     */
    async restart(): Promise<number> {
        this.stop();
        // 等待进程完全退出
        await new Promise(resolve => setTimeout(resolve, 500));
        return await this.start();
    }

    /**
     * 将文件路径转为PHP服务器URL
     */
    fileToUrl(fileFsPath: string): string | null {
        const port = this.port;
        if (!port) return null;

        const workspaceFolders = vscode.workspace.workspaceFolders;
        if (!workspaceFolders || workspaceFolders.length === 0) return null;

        const workspaceRoot = workspaceFolders[0].uri.fsPath;
        const serverPath = fileToServerPath(workspaceRoot, fileFsPath);

        return `http://${this.host}:${port}/${serverPath}`;
    }

    /**
     * 轮询等待服务器就绪
     */
    private async waitForServer(port: number, timeoutMs: number): Promise<void> {
        const start = Date.now();
        while (Date.now() - start < timeoutMs) {
            try {
                await httpGet(`http://${this.host}:${port}/`);
                return;
            } catch {
                await new Promise(resolve => setTimeout(resolve, 200));
            }
        }
        // 超时——不抛出错误，让调用方决定如何处理
    }

    /**
     * 检查PHP可执行文件是否存在
     */
    private async checkPhpExists(phpPath: string): Promise<boolean> {
        return new Promise((resolve) => {
            // 尝试直接运行 php -v
            const proc = child_process.spawn(phpPath, ['-v'], {
                windowsHide: true,
                stdio: ['ignore', 'pipe', 'pipe'],
            });
            proc.on('error', () => resolve(false));
            proc.on('exit', (code) => resolve(code === 0));
            setTimeout(() => resolve(false), 3000);
        });
    }

    /**
     * 释放资源
     */
    dispose(): void {
        this.stop();
        this._onStateChange.dispose();
    }
}
