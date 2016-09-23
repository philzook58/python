
'''
class Op:
    def __init__(self,label, index=()):
        self.label=label
        self.index=index
    def __str__(self):
        return self.label +  str(self.index)
    #def commute(self,b):
    #def __mul__(self,b):

#

a = Op('a',('i'))
adag = Op('adag',('j'))
delta= Op('delta',('i','j'))

expr = [a,adag]
print delta

'''
sumlist = [['a','a','a', 'adag', 'adag','adag']]
print sumlist
# another problem, I need to trickle constants to the back. Eh. Maybe that's not a problem.

#commuteone has to return a sumlist. Hence the double array signs
def commuteOne(expr):
    if expr == []:
        return [[1]]
    elif expr[-1]=='a':
        return [[0]]
    elif expr[0]=='adag':
        return [[0]]
    elif type(expr[0]) == int:
        return [expr]
    else:
        for i in range(len(expr)-1):
            if expr[i]=='a' and expr[i+1]=='adag':
                head = expr[0:i]
                if i+2 < len(expr):
                    tail = expr[i+2:]
                else:
                    tail = []
                expr1 = head + tail
                expr2 = head + ['adag','a'] + tail
                return [expr1, expr2]

for i in range(10):
    l = map(commuteOne,sumlist)
    sumlist = [item for sublist in l for item in sublist]
    print sumlist
    ''' # sum up all the numbers
    acc = 0
    for i in range(sumlist):
        if
        '''
sumlist = map(lambda x: x[0], sumlist)

print sumlist
print sum(sumlist)

# suggestion, describe priority. All daggers have higher priority or whatever.
# Sort according to priority.
#Normal ordering is sort of like sorting. With a monad? We carry along the sort structure.
#bubble sort is commuting
#mergesort is a relative of wick's thoerem. How to normal order two normal ordered expressions. :O::O: to :OO: by taking all pairs
#Wick's thoerem: Generate all pairs. Maybe that would be simpler
# the objects themselves should have flip rules.
#objects have a commutator and anticommutator dictionary #maybe just start with commutator
# or flipper

#def commutator(a,b):
#    if a == b
# return delta(i,j)
# if terms == ['a','b']:
#def match(terms):
#    switch case patterns
#def GenerateExp(, N):
    #return sumlist = [[1],[a],[1/2,a,a],etc]
# wildcards? implement dummy index equality
