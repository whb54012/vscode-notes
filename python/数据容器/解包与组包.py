# 对于所有容器包括字符串都能解包
zfc='1346'
mytuple=(1,3,4,6)
List=[1,2,3,5]
a1={1,3,4}
num1=1
num2=2
num=num1,num2
print(num)
# 定义数据容器的过程也可称为组包

a,b,c,d=zfc
print(d)
a,b,c=a1
print(c)
# 基础解包,将每个元素平均解开,元素与变量数量必须对应

g,*e,f=mytuple
print(e)
# *会将多出的剩余元素根据变量位置整合成列表