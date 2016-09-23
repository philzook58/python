
#State.
#The functions take raw state.
# The binding implements how we mold returned values into the raw state.raw state

#I'll implment state as a dictionary (this is not the most abstract thing I could do)
class State:
    def __init__(self,val= {}):
        self.value = val
    def bind(self,function):
        state = self.value
        returnval = function(state)
        print returnval
        for key, value in returnval.items():
            state[key] = value
        return State(state)
    def __rshift__(self,function):
        return self.bind(function)
    def __str__(self):
        return str(self.value)

#Initiliazie x to 3
print State() >> (lambda state: {'x', 3})
print State() >> (lambda state: {'x', 3}) >> (lambda state: {'x': state['x'] + 1})

#This still will have a ton of boilderplate. 
