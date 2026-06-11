import socket
import threading
def a(ip,port):
    sk = socket.socket()
    sk.settimeout(1)
    try:
        sk.connect((ip,port))
        print(port,"连接成功")
    except:
        print(port,"连接超时")
for i in range(100):
#利用循环同时开启多线程，几乎瞬间完成
    t = threading.Thread(target=a,args=(1,1))#创建一个线程对象为t
#target为调用的参数，将要调用的参数名写给他
#args为要传的参数，将形参以元组模式传过去
    t.start()
#启动线程，无需等待这个线程结果，直接开启下一循环
"""
创建一个线程对象 t（非常快，只是内存操作）。
调用 t.start()：通知操作系统 “这个线程可以开始调度了”，然后主线程立刻继续下一轮循环，不会等待这个线程执行完。
所以：
主线程在几毫秒内就把 100 个线程全部 “启动” 了，循环结束。
"""