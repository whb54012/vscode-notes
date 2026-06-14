"use strict";
var __createBinding = (this && this.__createBinding) || (Object.create ? (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    var desc = Object.getOwnPropertyDescriptor(m, k);
    if (!desc || ("get" in desc ? !m.__esModule : desc.writable || desc.configurable)) {
      desc = { enumerable: true, get: function() { return m[k]; } };
    }
    Object.defineProperty(o, k2, desc);
}) : (function(o, m, k, k2) {
    if (k2 === undefined) k2 = k;
    o[k2] = m[k];
}));
var __setModuleDefault = (this && this.__setModuleDefault) || (Object.create ? (function(o, v) {
    Object.defineProperty(o, "default", { enumerable: true, value: v });
}) : function(o, v) {
    o["default"] = v;
});
var __importStar = (this && this.__importStar) || (function () {
    var ownKeys = function(o) {
        ownKeys = Object.getOwnPropertyNames || function (o) {
            var ar = [];
            for (var k in o) if (Object.prototype.hasOwnProperty.call(o, k)) ar[ar.length] = k;
            return ar;
        };
        return ownKeys(o);
    };
    return function (mod) {
        if (mod && mod.__esModule) return mod;
        var result = {};
        if (mod != null) for (var k = ownKeys(mod), i = 0; i < k.length; i++) if (k[i] !== "default") __createBinding(result, mod, k[i]);
        __setModuleDefault(result, mod);
        return result;
    };
})();
Object.defineProperty(exports, "__esModule", { value: true });
exports.findFreePort = findFreePort;
exports.fileToServerPath = fileToServerPath;
exports.httpGet = httpGet;
const net = __importStar(require("net"));
const path = __importStar(require("path"));
const http = __importStar(require("http"));
/**
 * 查找空闲TCP端口，优先尝试指定端口
 */
function findFreePort(preferred) {
    return new Promise((resolve, reject) => {
        const server = net.createServer();
        server.on('error', (err) => {
            if (err.code === 'EADDRINUSE') {
                // 指定端口被占用，让OS分配
                server.listen(0, '127.0.0.1', () => {
                    const port = server.address().port;
                    server.close(() => resolve(port));
                });
            }
            else {
                reject(err);
            }
        });
        server.listen(preferred, '127.0.0.1', () => {
            const port = server.address().port;
            server.close(() => resolve(port));
        });
    });
}
/**
 * 将工作区中的文件路径转为URL编码的服务器路径
 * 处理中文文件名和Windows反斜杠
 */
function fileToServerPath(workspaceRoot, fileFsPath) {
    const relative = path.relative(workspaceRoot, fileFsPath);
    const forward = relative.replace(/\\/g, '/');
    return forward.split('/')
        .map(seg => encodeURIComponent(seg))
        .join('/');
}
/**
 * HTTP GET请求，用于检测服务器是否就绪
 */
function httpGet(url, timeout = 2000) {
    return new Promise((resolve, reject) => {
        const req = http.get(url, { timeout }, (res) => {
            let data = '';
            res.on('data', (chunk) => data += chunk);
            res.on('end', () => resolve(data));
        });
        req.on('error', reject);
        req.on('timeout', () => {
            req.destroy();
            reject(new Error('timeout'));
        });
    });
}
//# sourceMappingURL=utils.js.map