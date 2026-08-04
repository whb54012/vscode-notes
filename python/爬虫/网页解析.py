import lxml.html
with open("python\\爬虫\\读取网页.html","r",encoding="UTF-8") as f:
    reponse=f.read()
document=lxml.html.fromstring(reponse)
# 将html格式转换成一类对象
td_list=document.xpath("//div/tr/td/text()")
print(td_list)
# document.xpath("//标签/子标签/子标签/text()")
# 子标签写得越多抓取的越准确,最后一个不写标签而是目标格式
th_list=document.xpath("//div[1]/tr/td/text()")
print(th_list)
# 相同子标签太多时可用列表方法指定读取哪行子标签
t_list=document.xpath("//div/tr")
print(t_list)
# 想将每行子标签单独打印不放在一起,就读取上级子标签,然后将每个上级子标签打印
# 来进行分类
# for i in t_list:
#     pirnt(i/td)