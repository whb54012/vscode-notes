# 子类继承
class father:
    love="bask"
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def func(self):
        print("father")
    def prin(self):
        self.func()
        # 即使是在父类调用的func方法,可对象是子类,所以执行子类func方法而非父类

class son(father):
     def __init__(self,name,age):
            super().__init__(name,age)
            self.love=super().love
     def func(self):
            print("son")# 与父类方法重名
        
a=son("whb",18)# 继承父类属性
print(a.name,a.age,a.love)
a.prin()# 在父类里面执行子类方法

# 通过继承父类来动态执行子类没有的属性和方法,如子类拥有那就一定
# 执行子类,就算是再父类执行也是子类结果

print("-"*50)

# 父类继承
class father:
    def func(self):
        print("father")
    def prin(self):
        self.func()

class son(father):
     def func(self):
            print("son")
     def fther(self):
          super().func()
          #子类方法使用super()执行父类的func()方法
          father.func(self)
        #使用父类名方法让子类跳到父类上执行父类的func()方法
          
b=son()
b.fther()
# 通过两种方法使子类继承父类同名方法或属性