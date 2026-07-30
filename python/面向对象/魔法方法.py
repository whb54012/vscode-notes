# python类自动调用的方法
# __init__初始方法
# __str__转换成字符串
class fun:
    def __init__(self,name,age):
        self.age=age
        self.name=name
    def __str__(self):
        return f"姓名：{self.name}，年龄：{self.age}"