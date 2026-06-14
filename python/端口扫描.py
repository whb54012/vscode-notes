"""
socket.socket()启动后为一次性连接，连接完成后需要手动断开释放资源并重新赋予或者不初始化重新赋予一个套接字给变量
才可连接新端口
如若未初始化关闭前面的套接字,会导致就套接字遗失并在后台占用资源
"""
import socket
s = socket.socket()
"""通过套接字创造一个能够进行网络通信的对象"""
s.settimeout(1)
"""为套接字连接设置时间上限1s，超出时间限制将跳过此链接"""
a = ("www.baidu.com",80)
#网址加端口
s.connect(a)#以元组形式写入
#connect()网络连接
s.close()
"""将s这个对象断开并释放"""
"""重新赋予"""
s = socket.socket()
#创建新的套接字启用s对象
s.settimeout(2)
#设置时间
s.connect(("www.taobao.com",80))
#内部以元组形式(两种形式)写入网址加端口
s.close()
with open("C:\\Users\\whb\\Desktop\\常见网址.txt","r",encoding="utf-8") as f:
    wenben = f.readlines()
    for i in wenben:
        wen = i.replace("\n","")
        a = (wen,80)
        s=socket.socket()
        s.settimeout(2)
        try:
            s.connect(a)
            print(wen,"访问成功")
        except:
            print(wen,"连接超时")
        s.close()

