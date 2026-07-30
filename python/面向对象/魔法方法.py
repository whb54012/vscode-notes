# python类自动调用的方法
# __init__初始方法
# __str__转换成字符串
class Fun:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}"
    # 返回字符串模式
person=Fun('whb',18)
print(person)#打印返回的字符串