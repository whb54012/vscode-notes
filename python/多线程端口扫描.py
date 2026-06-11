import socket
import threading
import queue
def a(ip,p):
    while True:
        if p.empty():
            break
        port = p.get()
        sk = socket.socket()
        sk.settimeout(1)
        try:
            sk.connect((ip, port))
            print(port,"连接成功")
        except:
            pass
q = queue.Queue()
for i in range(5000):
    q.put(i)
for i in range(200):
    t = threading.Thread(target=a,args=("www.baidu.com",q))
    t.start()