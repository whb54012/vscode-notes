import lxml.html
with open("python\\爬虫\\读取网页.html","r",encoding="UTF-8") as f:
    reponse=f.read()
document=lxml.html.fromstring(reponse)
# 将html格式转换成文档对象

td_list=document.xpath("//div/tr/td/text()")
print(td_list)
# x.path把对象接收成列表
# document.xpath("//标签/子标签/子标签/text()")
# 子标签写得越多抓取的越准确
th_list=document.xpath("//div[1]/tr/td/text()")
print(th_list)
# 相同子标签太多时用列表方法指定读取哪行子标签

t_list=document.xpath("//div/tr")
print(t_list)#将父标签转换为对象列表
# 想将每行子标签内容单独打印,就读取上级父标签转换成对象列表,然后依次读取
# 每个对象来进行打印分类
for i in t_list:
    td=i.xpath("./td/text()")
    print(td)
# 通过循环分开打印每个对象里的子元素标签内容