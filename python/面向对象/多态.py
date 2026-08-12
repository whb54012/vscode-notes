class father:
    def __init__(self,name,age):
        self.name=name
        self.age=age
class pig(father):
    def se(self):
        print(f"{self.name}为{self.age}岁了")
class dog(father):
    def se(self):
        print(f"{self.name}为{self.age}岁了")
class cat(father):
    def se(self):
        print(f"{self.name}为{self.age}岁了")

def func(animal):
    animal.se()