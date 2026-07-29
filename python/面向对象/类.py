class Car:#类名首字母必须大写
    price=1000#静态添加属性,可修改
# 定义类
对象名=Car()
Car.name="bwm"#可动态添加修改属性
Car.color='red'
Car.price=10
print(Car.price)
print(Car.__dict__)
# 对象的内置函数,将对象属性按照字典格式打印
#                   类方法
class 类名:
    def __init__(self,参数):
        self.属性=参数
    # __init__初始化方法,创建对象自动调用
对象=类名('参数')

class Person:
    def __init__(self,name):
        pass

