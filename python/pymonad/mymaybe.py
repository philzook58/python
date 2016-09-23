

class Just:
    def __init__(self,val):
        self.value = val
    def bind(self,function):
        return function(self.value)
    def __rshift__(self,function):
        return self.bind(function)
    def __str__(self):
        return "Just(" + str(self.value) + ")"

class Nothing:
    def __init__(self):
        pass
    def bind(self,function):
        return self
    def __rshift__(self,function):
        return self.bind(function)
    def __str__(self):
        return "Nothing()"

# i think because of lack of currying, python puts parenthesis in a different place than haskell does
print Just(9) >> (lambda x: Just(x + 1))
print Just(9) >> (lambda x: Just(x + 1)) >> (lambda x: Just(x * 3))
print Just(9).bind(lambda x: Just(x + 1)).bind(lambda x: Just(x * 3))
print Nothing() >> (lambda x: Just(x + 1))
print Just(9) >> (lambda x: Just(x + 1)) >> (lambda x: Nothing())
print Just("Hello") >> (lambda x: Just(x + " World"))
