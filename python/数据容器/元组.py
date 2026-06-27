#                          2.元组 tuple
#一旦定义不可修改,只有查询和统计功能
#可存在不同类型和重复的元素，以()为标识,以[]为索引值
my_tuple = (1,"ni",3,4)
my_tuple1 = (1)
print(my_tuple)
print(my_tuple1)#当元组为一个元素时会被识别为算术的括号，打印结构将不会出现括号
print(my_tuple[2])#标识为()但索引值用[]不变

# 切片
print(my_tuple[0:5:1])