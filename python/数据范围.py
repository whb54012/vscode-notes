num=10#外界全局变量,已创建
def one(a,b):
    global num,sum#变量声明,不创建新变量,使用外界相同变量
# 如果外界不存在就以当前为全局变量并创建
    sum=a+b#创建全局变量sum
    num=1#使用外界已有全局变量num并修改
    return
one(1,2)
print(num)