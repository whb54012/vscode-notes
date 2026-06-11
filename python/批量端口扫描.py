import socket
def a(ip,port):
    sk = socket.socket()
    sk.settimeout(1)
    try:
        sk.connect((ip,port))
        print(port,"连接成功")
    except:
        print(port,"连接超时")
for i in range(1,100):
    a("192.168.1.7",i)
