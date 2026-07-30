class Car:#类名首字母必须大写
    price=1000#静态添加属性,可修改
# 定义类
对象名=Car()
对象名.name="bwm"#可动态添加属性
对象名.color='red'
对象名.price=10#可添加修改已有属性
print(对象名.price)
print(对象名.__dict__)
# 对象的内置函数,将对象属性按照字典格式打印
#                   类方法
class 类名:
    def __init__(self,参数):
        self.属性=参数
    # __init__初始化方法,创建对象自动调用
对象=类名('参数')

class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def fun(self,name):
        print(name)#打印传进来的参数
        print(self.name)#打印本身的name
person=Person('whb',18)
person.fun('w')
# 使用类方法时，对象会中断传一个对象变量过去
print(person.__dict__)

