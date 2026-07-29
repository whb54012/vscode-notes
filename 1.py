import requests
url=input()
cookie=input()
param=input()
data=input()
t=requests.get(url,data=data,params=param,cookies=cookie,timeout=1).text
t.find()