import requests
import threading
import warnings
import sys
print("Python输出编码:", sys.stdout.encoding)
input("按任意键继续...")
warnings.filterwarnings("ignore")
result=int(input("输入查找长度"))
url = input("输入url及注入点")
data=input("输入注入语句")
def fun(url,result,result2):
    for i in range(result2):
        try:
            reponse=requests.get(url+data.format(result,i))
            if '' in reponse.text:
                print(result,url+format(result,i),chr(i))
                break
        except:continue
    return
for  i in range(1,result):
    t=threading.Thread(target=fun,args=(url,result,150))
    t.start()