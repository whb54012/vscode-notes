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

                                # 字符串类型
# 字符串不可被修改,对字符串的修改都需要创建一个新变量去接受修改后的字符串
# 可以使指向原字符串的变量指向新字符串,达成对字符串修改的作用
zf = 'hello'
print(zf)
zf1 = "真的好 帅"#空格也算元素
#      1 2 3 4 5
print(zf1)#字符串用单引和多引都可以
#索引依旧使用[]
print(zf1[0])#从左到右
print(zf1[-1])#从右到左
#字符串替换方法：新字符串 = 字符串.replace(被替换的字符,替换的新字符)
#替换后原字符串不会变化，新字符串拥有替换后的结构
new_a = zf.replace('hello','你好')
#zf = zf.replace('hello','你好')
#或者将字符串修改后指向原字符串变量，原字符串就会被销毁回收并赋予新值
#注意,如果有多个相同'hello',所有'hello'都会被替换
print(zf)
print(new_a)
#如何决定替换的次数和个数
#1.count替换次数设置
new_b = zf.replace('l','i',1)
print(new_b)#只会替换一次
#指定位置替换
print(new_a+new_b+"ni")#字符串可以直接拼接


