from abc import ABC,abstractmethod
class father(ABC):
    def __init__(self):
        pass
    @abstractmethod# (抽象方法,子类如果没有这个函数就会报错)
    def must(self):
        pass
class son:
    def __init__(self):
        pass
    def must(self):# 提醒开发者子类要用自己的方法
        print("子类方法")
# 抽象化函数用于提醒,被抽象化的父类方法子类必须也有,没有就会报错提醒,用于
# 子类太多了忘记给子类添加方法的时候