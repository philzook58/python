from pymonad import *


class MyJust(Monad):
    def __init__(self,value):
        self.value = value
        super(MyJust, self).__init__()
    def bind(self, afunc):
        return afunc(self.value)

class MyNothing(Monad):
    def __init__(self):
        super(MyJust, self).__init__()
    def bind(self, afunc):
        return self

print MyJust(3) >> (lambda x: x * 2)
