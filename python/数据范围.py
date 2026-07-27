num=10
def one(a,b):
    global num#变量声明,全局变量
    num=a+b
    return
one(1,2)
print(num)