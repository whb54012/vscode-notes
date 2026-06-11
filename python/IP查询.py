#入门使用
#1.定义查询的域名
a = "www.baidu.com"
#2.导入socket模块，用关键字import使用
import socket
#3使用socket模块去查询ip
b = socket.gethostbyname(a)#存入ip
print(b)
print(socket.gethostbyname(a))#两种方法
with open("C:\\Users\\whb\\Desktop\\常见网址.txt","r",encoding="utf-8") as f:
    c = f.readlines()
    for i in c:
        #i.replace("\n","")无对象去接受值，无实际意义，仅展示将换行符替换
        try:
            # i = i.replace("\n","")1.创建对象去连接打印
            # socket.gethostbyname(i)
            socket.gethostbyname(i.replace("\n",""))#2.直接带入去连接
            print(socket.gethostbyname(i.replace("\n","")))
            l = i.strip("\n")#3.将首位特殊符去掉，可以去掉replace无法去掉的windows回车符
            print(socket.gethostbyname(l))
            print(i)
            #三种方法
        except:
            print("无法查询")
            print(i)