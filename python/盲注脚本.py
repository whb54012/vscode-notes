import requests
import queue
import threading
import warnings
warnings.filterwarnings("ignore")
num=int(input())
end=int(input())
url = input()
data=input()
def fun(url,result1):
    for i in range(num):
        if result1.empty():
            break
        num1=result1.get()
        reponse=requests.get(url.format(num)+data.format(num1))
        if '' in reponse.text:
            print(num,url.format(num)+data.format(num1),chr(num1))
        



result1=queue.Queue()
for i in range(1,end):
    result1.put(i)
    result1.empty
for  i in range(1,26):
    t=threading.Thread(target=fun,args=(url,result1))
    t.start()