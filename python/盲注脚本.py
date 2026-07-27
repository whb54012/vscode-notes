import requests
import queue
import threading
import warnings
warnings.filterwarnings("ignore")
result=int(input())
end=int(input())
url = input()
data=input()
def fun(url,result,result2):
    for i in result2:
        reponse=requests.get(url+data.format(result,result2))
        if '' in reponse.text:
            print(result,url+format(result,result2),chr(result2))
            break
for  i in range(1,end+1):
    t=threading.Thread(target=fun,args=(url,i,result))
    t.start()