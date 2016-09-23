
#State.
#The functions take raw state.
# The binding implements how we mold returned values into the raw state.raw state

#I'll implment state as a dictionary (this is not the most abstract thing I could do)
class State:
    def __init__(self,val= ({},{}) ):
        self.value = val
    def bind(self,function):
        state = self.value[1]
        for key, value in self.value[0].iteritems():
            state[key]=value
        print state
        return function(state)
    def __rshift__(self,function):
        return self.bind(function)
    def __str__(self):
        return str(self.value)

#Initiliazie x to 3
print State() >> (lambda state: State(({'x': 3}, state)))
print State() >> (lambda state: State(({'x': 3}, state))) >> (lambda state: State(({'x': state['x'] + 1}, state)))

#God. This is a train wreck.
#bind feels like its doing nothing for me.

#WHy shouldn't I just make functions that take states and output states? What does sepearting out the return value get me?
#Also, since I'm always passing through state, that's a ton of boilerplate.
#This can't be right.

#What i want is functions that take in state and output return values?
