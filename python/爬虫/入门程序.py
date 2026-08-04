import requests
url=input("url:")
# 定义url
reponse=requests.get(url=url)
# 读取对应网站源码
print(reponse)
