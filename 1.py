import requests
url=input()
cookie=input()
param=input()
str='-0123456789abcdefghijklmnopqrstuvwxyz{|}'
flag=""
data={

}
t=requests.get(url,data=data,params=param,cookies=cookie,timeout=1).text
if t.find("")>t.find(""):
    flag=flag+