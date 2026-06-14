import * as vscode from 'vscode';
import { PhpServerManager } from './phpServerManager';
import { PhpBrowserPanel } from './phpBrowserPanel';

let serverManager: PhpServerManager;
let browserPanel: PhpBrowserPanel;
let statusBarItem: vscode.StatusBarItem;

export function activate(context: vscode.ExtensionContext) {
    console.log('[PHP测试浏览器] 激活');

    serverManager = PhpServerManager.getInstance();
    browserPanel = PhpBrowserPanel.getInstance();

    // 状态栏
    statusBarItem = vscode.window.createStatusBarItem(
        vscode.StatusBarAlignment.Right,
        100
    );
    statusBarItem.command = 'phpBrowser.showPanel';
    statusBarItem.tooltip = '点击打开PHP测试浏览器面板';
    context.subscriptions.push(statusBarItem);

    // 更新状态栏
    const updateStatusBar = (state: string) => {
        if (state === 'running') {
            const port = serverManager.getPort();
            statusBarItem.text = `$(server) PHP:${port}`;
            statusBarItem.tooltip = `PHP服务器运行中 (端口 ${port})  点击打开浏览器面板`;
            statusBarItem.backgroundColor = undefined;
        } else {
            statusBarItem.text = `$(server) PHP已停止`;
            statusBarItem.tooltip = 'PHP服务器未运行  点击启动';
            statusBarItem.backgroundColor = new vscode.ThemeColor(
                'statusBarItem.warningBackground'
            );
        }
        statusBarItem.show();
    };

    // 初始状态
    updateStatusBar(serverManager.getState());
    // 监听状态变化
    context.subscriptions.push(
        serverManager.onStateChange(updateStatusBar)
    );

    // 注册命令
    const openCurrentCmd = vscode.commands.registerCommand(
        'phpBrowser.openCurrent',
        async () => {
            const editor = vscode.window.activeTextEditor;
            if (!editor) {
                vscode.window.showWarningMessage('请在编辑器中打开一个PHP文件');
                return;
            }
            const document = editor.document;
            if (document.languageId !== 'php') {
                vscode.window.showWarningMessage('当前文件不是PHP文件');
                return;
            }
            await browserPanel.openFile(document.uri.fsPath);
        }
    );

    const showPanelCmd = vscode.commands.registerCommand(
        'phpBrowser.showPanel',
        () => {
            browserPanel.show();
        }
    );

    const startServerCmd = vscode.commands.registerCommand(
        'phpBrowser.startServer',
        async () => {
            try {
                await vscode.window.withProgress(
                    {
                        location: vscode.ProgressLocation.Notification,
                        title: '正在启动PHP服务器...',
                    },
                    async () => {
                        await serverManager.start();
                    }
                );
                vscode.window.showInformationMessage(
                    `PHP服务器已启动: ${serverManager.getUrl()}`
                );
            } catch (err) {
                vscode.window.showErrorMessage(
                    `启动失败: ${err instanceof Error ? err.message : String(err)}`
                );
            }
        }
    );

    const stopServerCmd = vscode.commands.registerCommand(
        'phpBrowser.stopServer',
        () => {
            serverManager.stop();
            vscode.window.showInformationMessage('PHP服务器已停止');
        }
    );

    const refreshCmd = vscode.commands.registerCommand(
        'phpBrowser.refresh',
        () => {
            browserPanel.refresh();
        }
    );

    context.subscriptions.push(
        openCurrentCmd,
        showPanelCmd,
        startServerCmd,
        stopServerCmd,
        refreshCmd
    );
}

export function deactivate() {
    console.log('[PHP测试浏览器] 停用');
    if (serverManager) {
        serverManager.dispose();
    }
    if (browserPanel) {
        browserPanel.dispose();
    }
}
