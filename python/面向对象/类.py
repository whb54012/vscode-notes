class Car:#类名首字母必须大写
    price=1000
# 定义类

对象名=Car()
Car.name="bwm"#可动态添加属性
Car.color='red'

print(Car.__dict__)
# 对象的内置函数,将对象属性按照字典格式打印
