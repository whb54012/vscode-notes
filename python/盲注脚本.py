import requests
import queue
import threading
import warnings
warnings.filterwarnings("ignore")
word=""
end=int(input())
url = input()
data=input()
def fun(url,result1,result2):
    reponse=requests.get(url.format(result1.get())+data.format(result2.get()))



result1=queue.Queue()
result2=queue.Queue()
for i in range(1,end):
    result1.put(i)
    result2.put(i)
for  i in range(1,26):
    t=threading.Thread(target=fun,args=(url,result1,result2))
    t.start()