class father:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class p(father):
    def se(self):
        print(f"{self.name}为{self.age}岁了")
class d(father):
    def se(self):
        print(f"{self.name}为{self.age}岁了")
class c(father):
    def se(self):
        print(f"{self.name}为{self.age}岁了")

def func(animal):
    animal.se()# 通过函数调用属性里的方法
# 多态:只用一个入口就能表示多个输出

func(p("pig",1))
func(d("dog",2))
func(c("cat",3))
# 使用外置函数创建对象属性并调用对象各自的方法