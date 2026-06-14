import * as net from 'net';
import * as path from 'path';
import * as http from 'http';

/**
 * 查找空闲TCP端口，优先尝试指定端口
 */
export function findFreePort(preferred: number): Promise<number> {
    return new Promise((resolve, reject) => {
        const server = net.createServer();
        server.on('error', (err: NodeJS.ErrnoException) => {
            if (err.code === 'EADDRINUSE') {
                // 指定端口被占用，让OS分配
                server.listen(0, '127.0.0.1', () => {
                    const port = (server.address() as net.AddressInfo).port;
                    server.close(() => resolve(port));
                });
            } else {
                reject(err);
            }
        });
        server.listen(preferred, '127.0.0.1', () => {
            const port = (server.address() as net.AddressInfo).port;
            server.close(() => resolve(port));
        });
    });
}

/**
 * 将工作区中的文件路径转为URL编码的服务器路径
 * 处理中文文件名和Windows反斜杠
 */
export function fileToServerPath(workspaceRoot: string, fileFsPath: string): string {
    const relative = path.relative(workspaceRoot, fileFsPath);
    const forward = relative.replace(/\\/g, '/');
    return forward.split('/')
        .map(seg => encodeURIComponent(seg))
        .join('/');
}

/**
 * HTTP GET请求，用于检测服务器是否就绪
 */
export function httpGet(url: string, timeout: number = 2000): Promise<string> {
    return new Promise((resolve, reject) => {
        const req = http.get(url, { timeout }, (res) => {
            let data = '';
            res.on('data', (chunk: string) => data += chunk);
            res.on('end', () => resolve(data));
        });
        req.on('error', reject);
        req.on('timeout', () => {
            req.destroy();
            reject(new Error('timeout'));
        });
    });
}
