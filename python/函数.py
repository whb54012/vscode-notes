def 自定义变量名(x):
    print(x) #缩进不能忘，默认四格没有返回值就不写return 返回值这句话
x=""
自定义变量名(x)

#函数关键字def
def two():
    print(2,"你好")#用逗号隔开
two()
#函数生效必须调用后才有值

#传参方式
# 1.顺序传参
def one(a,b):
    print(a+b)
one()

# 2# 关键值传参
def zhi(c,d):
    print(c+d)
zhi(d=1,c=2)

# 不定长传参
def three(*arg):#将吸收的参数结合为元组
    print(sum(arg))
three(1,2,3,4,5,6)

#设置默认参数
def jia(a,b=300):#为b设置默认值，当b没有参数传进时，默认为300,注意带默认值的参数
#必须放在无默认值参数的右边,否则会报错
    print(a+b)
jia(100,200)#传参
jia(100)#b不传参，用默认值使用
def zfc(c,d="nihao"):
    print(c+"和"+d)#字符串拼接用+号，汉字用字符串表示
    print(f"{c}和{d}")
zfc('whb')
#有返回值记得加return



# 绑定形参关键字,此时不依赖顺序
def a():
    pass
#pass代表空的意思，表示此函数还未开始使用，只是占据了位置