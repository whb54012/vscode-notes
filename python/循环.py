#                               for循环
"""用于列表/元组/字符串/集合/字典循环"""
"""for 变量名 in 变量:
    循环的代码
"""
a = ["12","23","34"]
b = (1,2,3)
c = "abc"
print(a)
print(b)
for i in b:
    print(b)
for i in a:
    print(i)#必须缩进
for i in c:
    print(c)#字符串也可以遍历
#每循环一次取出内部的一个值
for i in range(1,4):#两个数表示从第一个数循环到第二个数之前(不包含它本身)
    print(i)
#控制for循环次数,
for i in range(4):#()一个数表示从零开始到输入数之前(不包含本身)
    print(i)
for i in range(1,10,2):#为三个数时第三个数表示到下个数的步长
    print(i)
#                               while循环
#根据条件循环
"""
    while 条件判断:
        循环体内容
"""
b = 0
while b < 10:
    print(b)
    b += 1#python中不包含b++这种自增符号
print(b)#通过缩进来决定是否在循环内部
