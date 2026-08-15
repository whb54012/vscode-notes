import requests,threading,hashlib
minute=input("输入时分")
url=input("输入网址")
with open("C:\\Users\\whb\\Downloads\\key (1).dat","rb")as f:
    data1=f.read()
    data2="mmmmmmm"
def func(data):
    reponse=requests.post(url=url,data=data,verify=False)
    with lock:
        print(reponse.text()+"\n")
for i in range(1000):
    thred=[]
    therd=threading.Thread(target=func,args=(data1,))
    therd=threading.Thread(target=func,args=(data2,))
lock=threading.Lock()
for i in range(2000): therd[i].start()
    