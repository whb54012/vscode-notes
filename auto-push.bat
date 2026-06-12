@echo off
cd /d C:\Users\whb\Desktop\vscode
git add -A
git diff --cached --quiet
if %errorlevel% equ 0 (
    echo [%date% %time%] 无变更，跳过推送 >> auto-push.log
) else (
    git commit -m "自动提交：%date% %time%"
    git push >> auto-push.log 2>&1
    echo [%date% %time%] 已推送到 GitHub >> auto-push.log
)
