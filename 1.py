import requests
url=input()
cookie=input()
data=input()
t=requests.post(url,data=data,cookies=cookie,timeout=1).text
