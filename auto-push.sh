#!/bin/bash
cd /c/Users/whb/Desktop/vscode
while true; do
  git add -A
  if git diff --cached --quiet; then
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 无变更，跳过推送"
  else
    git commit -m "自动提交：$(date '+%Y-%m-%d %H:%M:%S')"
    git push
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] 已推送到 GitHub"
  fi
  echo "[$(date '+%Y-%m-%d %H:%M:%S')] 等待1小时后再次检查..."
  sleep 3600
done
