import requests
url=input()
cookie=input()
param=input()
t=requests.get(url,params=param,cookies=cookie,timeout=1).text
