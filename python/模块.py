import 模块名
# 启动模块
import 模块名 as 别名
# 用别名来调用模块
from 模块名 import 功能名
# 直接导入功能名，使用功能不用再写模块名
from 模块名 import *
# 导入所有功能名,使用所有功能不再写模块名
from 模块名 import 功能名 as 别名
# 用别名来调用功能

# 自定义模块被运行时和被当作模块导入运行时__name__参数不同,由此限制他被当作
# 模块导入时不该执行哪些功能
if __name__=='__main__':
    def 函数():
        print("函数被创建")
"""注意,python用条件或循环创建出来的函数或变量不会因为被执行完毕后就销毁,会一直
保留到主程序结束"""

# 自定义导入功能,使用from 模块名 import *时可以用__all__来限制导入部分
__all__ = ['public_func', 'PublicClass','b']  # 声明公开接口
def public_func():
    print("我是公开函数")
class PublicClass:
    pass
a=1
b=2
def _private_func():
    print("我是私有函数（下划线开头）")
