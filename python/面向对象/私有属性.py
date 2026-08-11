class preson:
    def __init__(self,name,age):
        self.name=name
        self.age=age
        self.__high=180# 熟悉名在外部被改为_preson_high
        print(self.__high)# 在内部直接用原名读取

    def __love(self):# 方法名在外部被系统修改为_preson__love
        self.love="bask"
        print(a.love)
a=preson("whb",20)
print(a.age,a.name)
# 正常读出

# a.__love和printprint(a.__high)在外部无法执行,找不到方法名

a._preson__love()
print(a._preson__high)
# 在外部正常执行私有方法和私有属性

# 注意,python没有真正意义上的私有属性
# 私有原理是python类属性方法除了魔术方法以外,其他方法和属性在外部加上双下划线会被
# 系统重新命名成_类名__属性/方法名,让你读取时在外部调用使用原名会找不到方法从而失
# 败造成的伪私有属性,只要按照_类名__属性/方法名照样能运行