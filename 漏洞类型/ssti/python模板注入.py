# __class__:检查对象的类型
变量/类.__class__:元素的类型

# 对象是带有构造函数的类型时:
# __init__:拿出函数对象object,前面必须是带有构造函数的类
class cat:
    def __init__(self):
        pass
类.__class__.__init__
# 类.__class__.__init__.__globals__:取出模块的全局字典






# 对象是不带有构造函数init的类型时:
# __base__:显示元素的父类:用于非类元素而是变量的类型
"hi".__class__.__base__: