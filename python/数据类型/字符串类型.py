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

"""替换(replace)"""
# 新字符串=字符串.replace('查找值'，'替换值','替换次数')
new_a = zf.replace('hello','你好')
print(new_a)
#替换后原字符串不会变化，新字符串拥有替换后的结构
zf = zf.replace('hello','你好')
#或者将字符串修改后指向原字符串变量
#注意,如果有多个相同'hello',所有'hello'都会被替换
print(zf)
new_b = zf.replace('l','i',1)
print(new_b)#只会替换一次
print(new_a+new_b+"ni")#字符串可以直接拼接

"""查找统计(find,count)"""
zf.find('he')
# 返回字符串中查找字串第一次出现的索引位置,找不到旧返回-1
zf.count('he')
# 统计字串出现的次数

"""转换(upper,lower)"""
zf.upper()#将字串的字母转换为大写写
zf.lower()#将字串的字母转换为小写


# 切片
zf[0:5:2]
print(zf[0:5:2])
# 用法和拓展跟列表切片如一