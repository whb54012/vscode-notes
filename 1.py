import os
class cat():
    def __init__(self):
        abc='123'
print(cat().__class__.__init__.__globals__['os'].popen('id').read())