import os
class cat():
    def __init__(self):
        pass
print(cat().__class__.__init__.__globals__['os'].popen('id').read())