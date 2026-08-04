import requests
import lxml
url=input("url:")
# 定义url
reponse=requests.get(url=url).text
# 读取对应网站源码并转换为text格式
print(reponse)
# 读取网站源码为text格式

