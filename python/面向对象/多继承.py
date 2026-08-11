# 方法一:
class fa1:
    def __init__(self,name):
        self.name=name
class fa2:
     def __init__(self,age):
         self.age=age
# 注意,多继承里面出现同名函数会默认先继承第一个

class son(fa1,fa2):
    def __init__(self,name,age):
        fa1.__init__(self,name)
        fa2.__init__(self,age)
        # 通过构造函数将两个父级调用,用各自类名指定
person=son("whb",19)
print(person.name,person.age)

# 方法二:
class fa1:
    def __init__(self,name,age):
        super().__init__(age)
        # 通过super()函数将下一个父类fa2的方法继承调用
        self.name=name
class fa2:
     def __init__(self,age):
         self.age=age
# 注意,多继承里面出现同名函数会默认先继承第一个

class son(fa1,fa2):#链条顺序fa1-fa2
    pass
person=son("whb",19)
print(person.name,person.age)
