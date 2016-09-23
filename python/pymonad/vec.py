
#Vectors are lists (the list is assumed to mean sum) of pairs of (multipliers, basis vector descriptor)

#function expect a basis vector and output a true list vector

class Vector:
    def __init__(self,val=[(None,None)]):
        self.value = val
    def collect(self):
        self.value = sorted(self.value, key= (lambda (mult,basis): basis))

        return self
    def bind(self,function):
        outvec = []
        for term in self.value:
            retvec = function(term[1])
            outvec = outvec + map(lambda (mult, basisvec): (term[0]* mult, basisvec), retvec)
        return Vector(outvec).collect()
    def __rshift__(self,function):
        return self.bind(function)
    def __str__(self):
        return reduce(lambda a, b: a + ' + ' + b, map(lambda (mult, base): str(mult) + base ,self.value))

r = Vector([(3,'x'), (3,'y'), (4,'z')])
print r

def scalarmult(basis,mult):
    return [(mult,basis)]

def linop(basis):
    if basis == 'x':
        return [(3,'y')]
    elif basis == 'y':
        return [(3,'z'),(4,'x')]
    elif basis == 'z':
        return [(3,'z'),(4,'x')]

print r >> linop

'''
def convertMatrixtoOp(matrix):
    def linop(basis):
        if basis == 'x':

        elif basis == 'y':

        elif basis == 'z':
    return linop
'''
