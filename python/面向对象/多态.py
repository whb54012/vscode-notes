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
    animal.se()
func(p("pig",1))
func(d("dog",2))
func(c("cat",3))