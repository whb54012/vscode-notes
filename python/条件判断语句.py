# if else判断
age = input("你的年龄？")#数据类型永远是字符串
age = int(age)# 强制转换
if age < 18:
    print(1)
elif age <= 70:
#elif类似与C语言else if 嵌合体
    print(2)
else:
    print(3)
#break在循环中使用来断绝无限循环
# match case判断
# case后面可以根据需求自定义匹配任何类型
a = int(input("请输入数字"))
match a:
    case 1:
        print(1)
    case 2:
        print(2)
    case 3:
        print(3)
    case 4:
        print(4)
    case 5:
        print(5)
    case 6 | 7:# |表示或的关系，只要其中一个符合就行，这里不可用o
        print(6,7)
    case _:
        print("else")#_代表其他所有选择，类似于default