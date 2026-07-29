import requests
url=input()
cookie=input()
data=input()
requests.post(url,data=data,cookies=cookie,)