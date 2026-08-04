import requests
import lxml
url=input("url:")
# 定义url
reponse=requests.get(url=url).text
# 读取对应网站源码并转换为text格式
document=lxml.html.fromastring(reponse)
# 将html格式转换成一类对象
print(document)
