import requests
import lxml.html
url=input("url:")
# 定义url
reponse=requests.get(url=url).text
# 读取对应网站源码并转换为text格式
document=lxml.html.fromstring(reponse)
# 将html格式转换成一类对象
document.xpath("//标签/子标签/子标签/text()")
# 子标签写得越多抓取的越准确,最后一个不写标签而是目标格式
document.xpath("//标签/子标签/子标签[1]/text()")
# 相同子标签太多时可指定读取哪一行