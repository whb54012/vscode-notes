import socket
c = ".baidu.com"#百度子域名查询
with open("C:\\Users\\whb\\Desktop\\常见子域名.txt","r",encoding="utf-8") as f:
    a = f.readlines()
    for i in a:
        b = i.replace("\n","")
        new = b+c
        try:
            print(socket.gethostbyname(new))
            print(new)
        except:
            print("错误")
            print(new)

