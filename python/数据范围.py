num=10
def one(a,b):
    global num,sum#变量声明,与外部全局变量指向同一个
# ,如果外部不存在就以当前未全局变量
    sum=a+b
    num=1
    return
one(1,2)
print(num)