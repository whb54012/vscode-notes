import * as vscode from 'vscode';
import { PhpServerManager } from './phpServerManager';

/**
 * 嵌入式PHP浏览器面板
 * 使用Webview + iframe加载PHP服务器页面
 */
export class PhpBrowserPanel {
    private static instance: PhpBrowserPanel;

    private panel: vscode.WebviewPanel | null = null;
    private serverManager: PhpServerManager;
    private currentUrl: string = '';
    private homeUrl: string = '';

    // 导航历史
    private history: string[] = [];
    private historyIndex: number = -1;

    private constructor() {
        this.serverManager = PhpServerManager.getInstance();

        // 监听服务器状态变化
        this.serverManager.onStateChange((state) => {
            this.updateServerStatus(state);
        });
    }

    static getInstance(): PhpBrowserPanel {
        if (!PhpBrowserPanel.instance) {
            PhpBrowserPanel.instance = new PhpBrowserPanel();
        }
        return PhpBrowserPanel.instance;
    }

    /**
     * 显示浏览器面板
     */
    show(): void {
        if (this.panel) {
            this.panel.reveal(vscode.ViewColumn.Beside);
            return;
        }

        this.panel = vscode.window.createWebviewPanel(
            'phpBrowser',
            'PHP测试浏览器',
            vscode.ViewColumn.Beside,
            {
                enableScripts: true,
                retainContextWhenHidden: true,
                localResourceRoots: [],
            }
        );

        this.panel.iconPath = vscode.Uri.parse(
            'data:image/svg+xml,' + encodeURIComponent(
                '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24"><text y="18" font-size="18">🐘</text></svg>'
            )
        );

        // 监听面板关闭
        this.panel.onDidDispose(() => {
            this.panel = null;
            vscode.commands.executeCommand('setContext', 'phpBrowserPanelVisible', false);
        });

        // 监听来自Webview的消息
        this.panel.webview.onDidReceiveMessage(
            this.handleMessage.bind(this)
        );

        vscode.commands.executeCommand('setContext', 'phpBrowserPanelVisible', true);

        // 更新内容
        this.updateWebviewContent();
        this.updateServerStatus(this.serverManager.getState());
    }

    /**
     * 在浏览器中打开指定文件
     */
    async openFile(filePath: string): Promise<void> {
        this.show();

        // 确保服务器在运行
        if (!this.serverManager.isRunning()) {
            try {
                await this.serverManager.start();
            } catch (err) {
                vscode.window.showErrorMessage(
                    `无法启动PHP服务器: ${err instanceof Error ? err.message : String(err)}`
                );
                return;
            }
        }

        const url = this.serverManager.fileToUrl(filePath);
        if (url) {
            this.navigateTo(url);
        }
    }

    /**
     * 导航到指定URL
     */
    navigateTo(url: string): void {
        this.currentUrl = url;

        // 添加到历史记录
        if (this.historyIndex < this.history.length - 1) {
            this.history = this.history.slice(0, this.historyIndex + 1);
        }
        this.history.push(url);
        this.historyIndex = this.history.length - 1;

        this.postMessageToWebview({
            type: 'navigate',
            url: url,
        });
        this.updateBackForwardState();
    }

    /**
     * 刷新当前页面
     */
    refresh(): void {
        if (this.currentUrl) {
            this.postMessageToWebview({
                type: 'navigate',
                url: this.currentUrl,
            });
        }
    }

    /**
     * 导航到主页
     */
    private navigateHome(): void {
        if (this.homeUrl) {
            this.navigateTo(this.homeUrl);
        } else {
            // 默认主页：显示PHP信息
            const baseUrl = this.serverManager.getUrl();
            if (baseUrl) {
                this.navigateTo(baseUrl);
            }
        }
    }

    /**
     * 释放资源
     */
    dispose(): void {
        if (this.panel) {
            this.panel.dispose();
            this.panel = null;
        }
    }

    /**
     * 生成Webview HTML内容
     */
    private getHtmlContent(): string {
        const csp = [
            `default-src 'none'`,
            `style-src 'unsafe-inline'`,
            `script-src 'unsafe-inline'`,
            `frame-src http://127.0.0.1:* http://localhost:*`,
            `connect-src http://127.0.0.1:* http://localhost:*`,
            `img-src http://127.0.0.1:* http://localhost:* data:`,
        ].join('; ');

        return `<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="Content-Security-Policy" content="${csp}">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>PHP测试浏览器</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            display: flex;
            flex-direction: column;
            height: 100vh;
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Tahoma, sans-serif;
            font-size: 13px;
        }
        #toolbar {
            display: flex;
            align-items: center;
            gap: 4px;
            padding: 4px 8px;
            background: var(--vscode-sideBar-background, #f3f3f3);
            border-bottom: 1px solid var(--vscode-sideBar-border, #e0e0e0);
            flex-shrink: 0;
        }
        #toolbar button {
            background: none;
            border: none;
            cursor: pointer;
            padding: 4px 6px;
            color: var(--vscode-foreground, #333);
            font-size: 14px;
            border-radius: 4px;
            display: flex;
            align-items: center;
            justify-content: center;
            min-width: 28px;
            min-height: 24px;
        }
        #toolbar button:hover {
            background: var(--vscode-toolbar-hoverBackground, rgba(0,0,0,0.1));
        }
        #toolbar button:disabled {
            opacity: 0.35;
            cursor: default;
        }
        #urlBar {
            flex: 1;
            margin: 0 4px;
            padding: 3px 8px;
            border: 1px solid var(--vscode-input-border, #ccc);
            background: var(--vscode-input-background, #fff);
            color: var(--vscode-input-foreground, #333);
            border-radius: 3px;
            font-size: 13px;
            outline: none;
            min-width: 0;
        }
        #urlBar:focus {
            border-color: var(--vscode-focusBorder, #007acc);
        }
        #content {
            flex: 1;
            border: none;
            width: 100%;
            background: white;
        }
        #statusBar {
            display: flex;
            align-items: center;
            gap: 6px;
            padding: 2px 8px;
            font-size: 12px;
            background: var(--vscode-statusBar-background, #007acc);
            color: var(--vscode-statusBar-foreground, #fff);
            flex-shrink: 0;
        }
        .status-dot {
            width: 8px;
            height: 8px;
            border-radius: 50%;
            display: inline-block;
            flex-shrink: 0;
        }
        .status-dot.running { background: #4ec94e; }
        .status-dot.stopped { background: #cc4444; }
        .status-dot.starting { background: #f0ad4e; animation: pulse 1s infinite; }
        @keyframes pulse {
            0%, 100% { opacity: 1; }
            50% { opacity: 0.4; }
        }
        #serverStatus { flex: 1; }
        #errorOverlay {
            display: none;
            position: absolute;
            top: 40px; left: 0; right: 0; bottom: 24px;
            background: rgba(0,0,0,0.03);
            justify-content: center;
            align-items: center;
            z-index: 10;
            pointer-events: none;
        }
        #errorOverlay.visible {
            display: flex;
        }
        .error-box {
            background: var(--vscode-editor-background, #fff);
            border: 1px solid var(--vscode-inputValidation-errorBorder, #e74c3c);
            border-radius: 6px;
            padding: 20px 28px;
            max-width: 420px;
            text-align: center;
            box-shadow: 0 4px 12px rgba(0,0,0,0.15);
            pointer-events: auto;
        }
        .error-box h3 { margin-bottom: 8px; font-size: 16px; }
        .error-box p { color: var(--vscode-descriptionForeground, #666); line-height: 1.5; }
        .error-box button {
            margin-top: 12px;
            padding: 6px 16px;
            background: var(--vscode-button-background, #007acc);
            color: var(--vscode-button-foreground, #fff);
            border: none;
            border-radius: 3px;
            cursor: pointer;
        }
        .loading-indicator {
            position: absolute;
            top: 40px; left: 0; right: 0;
            height: 3px;
            z-index: 5;
            background: linear-gradient(90deg, transparent, var(--vscode-progressBar-background, #007acc), transparent);
            background-size: 200% 100%;
            animation: loadingSlide 1.5s infinite;
            display: none;
        }
        .loading-indicator.visible { display: block; }
        @keyframes loadingSlide {
            0% { background-position: 200% 0; }
            100% { background-position: -200% 0; }
        }
    </style>
</head>
<body>
    <div id="toolbar">
        <button id="btnBack" title="后退" onclick="sendMsg('back')">&#9664;</button>
        <button id="btnForward" title="前进" onclick="sendMsg('forward')">&#9654;</button>
        <button id="btnRefresh" title="刷新" onclick="sendMsg('refresh')">&#x21bb;</button>
        <button id="btnHome" title="主页" onclick="sendMsg('home')">&#x2302;</button>
        <input type="text" id="urlBar" placeholder="输入URL..."
               onkeydown="if(event.key==='Enter'){loadUrl(this.value)}">
    </div>
    <div class="loading-indicator" id="loadingIndicator"></div>
    <iframe id="content" sandbox="allow-scripts allow-forms allow-same-origin"
            src="about:blank"
            onload="onIframeLoad()"></iframe>
    <div id="errorOverlay">
        <div class="error-box">
            <h3>&#x26A0; 无法加载页面</h3>
            <p id="errorMessage">请检查PHP服务器是否已启动</p>
            <button onclick="sendMsg('retry')">重试</button>
        </div>
    </div>
    <div id="statusBar">
        <span class="status-dot stopped" id="serverDot"></span>
        <span id="serverStatus">服务器未连接</span>
        <span id="urlDisplay" style="opacity:0.7;overflow:hidden;text-overflow:ellipsis;white-space:nowrap;direction:rtl;text-align:right;max-width:40%;"></span>
    </div>
    <script>
        (function() {
            const vscode = acquireVsCodeApi();
            const iframe = document.getElementById('content');
            const urlBar = document.getElementById('urlBar');
            const btnBack = document.getElementById('btnBack');
            const btnForward = document.getElementById('btnForward');
            const btnRefresh = document.getElementById('btnRefresh');
            const loadingIndicator = document.getElementById('loadingIndicator');
            const errorOverlay = document.getElementById('errorOverlay');
            const urlDisplay = document.getElementById('urlDisplay');

            let currentUrl = '';
            let isLoading = false;
            let loadTimer = null;

            // 从vscode状态恢复
            const savedState = vscode.getState();
            if (savedState && savedState.url) {
                currentUrl = savedState.url;
            }

            function loadUrl(url) {
                if (!url) return;
                if (!url.startsWith('http://') && !url.startsWith('https://')) {
                    url = 'http://' + url;
                }
                currentUrl = url;
                iframe.src = url;
                urlBar.value = url;
                urlDisplay.textContent = url;
                showLoading(true);
                errorOverlay.classList.remove('visible');
                vscode.postMessage({ type: 'navigated', url: url });
            }

            function showLoading(show) {
                isLoading = show;
                loadingIndicator.classList.toggle('visible', show);
                if (show) {
                    clearTimeout(loadTimer);
                    loadTimer = setTimeout(function() {
                        // 10秒后如果还在加载，停止loading动画
                        loadingIndicator.classList.remove('visible');
                    }, 10000);
                }
            }

            function onIframeLoad() {
                showLoading(false);
                try {
                    var href = iframe.contentWindow.location.href;
                    if (href && href !== 'about:blank') {
                        currentUrl = href;
                        urlBar.value = href;
                        urlDisplay.textContent = href;
                    }
                } catch(e) {
                    // 跨域无法读取URL，忽略
                }
            }

            function sendMsg(type) {
                vscode.postMessage({ type: type });
            }

            // 监听来自extension的消息
            window.addEventListener('message', function(event) {
                var msg = event.data;
                if (!msg) return;
                switch (msg.type) {
                    case 'navigate':
                        loadUrl(msg.url);
                        break;
                    case 'serverStatus':
                        var dot = document.getElementById('serverDot');
                        var status = document.getElementById('serverStatus');
                        dot.className = 'status-dot ' + msg.serverState;
                        var texts = {
                            'running': 'PHP服务器运行中 (端口 ' + msg.port + ')',
                            'starting': 'PHP服务器启动中...',
                            'stopped': 'PHP服务器未运行'
                        };
                        status.textContent = texts[msg.serverState] || '未知状态';
                        btnRefresh.disabled = msg.serverState !== 'running';
                        if (msg.serverState === 'stopped' && currentUrl) {
                            errorOverlay.classList.add('visible');
                            document.getElementById('errorMessage').textContent =
                                'PHP服务器已停止，请启动服务器后重试';
                        } else {
                            errorOverlay.classList.remove('visible');
                        }
                        break;
                    case 'backForwardState':
                        btnBack.disabled = !msg.canGoBack;
                        btnForward.disabled = !msg.canGoForward;
                        break;
                    case 'error':
                        errorOverlay.classList.add('visible');
                        document.getElementById('errorMessage').textContent =
                            msg.message || '发生未知错误';
                        showLoading(false);
                        break;
                }
            });

            // 暴露全局函数
            window.loadUrl = loadUrl;
            window.onIframeLoad = onIframeLoad;
            window.sendMsg = sendMsg;

            // 恢复之前的URL
            if (currentUrl) {
                loadUrl(currentUrl);
            }
        })();
    </script>
</body>
</html>`;
    }

    /**
     * 更新Webview内容
     */
    private updateWebviewContent(): void {
        if (this.panel) {
            this.panel.webview.html = this.getHtmlContent();
        }
    }

    /**
     * 向Webview发送消息
     */
    private postMessageToWebview(message: any): void {
        if (this.panel) {
            this.panel.webview.postMessage(message);
        }
    }

    /**
     * 更新服务器状态显示
     */
    private updateServerStatus(state: string): void {
        const url = this.serverManager.getUrl();
        const port = this.serverManager.getPort();

        this.postMessageToWebview({
            type: 'serverStatus',
            serverState: state,
            port: port,
            url: url,
        });
    }

    /**
     * 更新前进/后退按钮状态
     */
    private updateBackForwardState(): void {
        this.postMessageToWebview({
            type: 'backForwardState',
            canGoBack: this.historyIndex > 0,
            canGoForward: this.historyIndex < this.history.length - 1,
        });
    }

    /**
     * 处理来自Webview的消息
     */
    private handleMessage(message: any): void {
        switch (message.type) {
            case 'navigated':
                // 更新历史记录
                if (this.historyIndex < this.history.length - 1) {
                    this.history = this.history.slice(0, this.historyIndex + 1);
                }
                this.history.push(message.url);
                this.historyIndex = this.history.length - 1;
                this.currentUrl = message.url;
                this.updateBackForwardState();
                break;

            case 'back':
                if (this.historyIndex > 0) {
                    this.historyIndex--;
                    this.currentUrl = this.history[this.historyIndex];
                    this.postMessageToWebview({
                        type: 'navigate',
                        url: this.currentUrl,
                    });
                    this.updateBackForwardState();
                }
                break;

            case 'forward':
                if (this.historyIndex < this.history.length - 1) {
                    this.historyIndex++;
                    this.currentUrl = this.history[this.historyIndex];
                    this.postMessageToWebview({
                        type: 'navigate',
                        url: this.currentUrl,
                    });
                    this.updateBackForwardState();
                }
                break;

            case 'refresh':
                this.refresh();
                break;

            case 'home':
                this.navigateHome();
                break;

            case 'retry':
                if (this.currentUrl) {
                    this.refresh();
                }
                break;
        }
    }
}
