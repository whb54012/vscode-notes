                                # 数值类型
"""数值类型为可修改类型，无需拿新对象接受修改后的新值"""
a1 = 1 #整数类型
b1 = 1.2 #浮点数类型
c1 = True+1
d = False#布尔类型(首字母必须为大写)
# 不同布尔值进行运算都会变成数字型布尔值
d1 = d+1
#变量设置
a = 10
#打印函数
print(a1)
print(b1)
print(c1)
print(d)
print(d1)
print(type(a1))#type()显示其类型
isinstance(a1,int)#判断其类型,正确就为true，否则就为false