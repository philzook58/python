class Symbol:
    def __init__(self,name):
        self.label = name

psi = Symbol("psi")

class Op:
    def __init__(self,name, leaf1=None,leaf2=None):
        self.label=name
        self.leaf1 = leaf1
        self.leaf2 = leaf2

#root = Symbol('root')
mul = Op('mul', psi, psi)
mul2 = Op('mul', psi, mul)

def traversePrint(tree):
    print tree.label
    if isinstance(tree,Op):
        traversePrint(tree.leaf1)
        traversePrint(tree.leaf2)
    #elif type(tree) == Symbol:

traversePrint(mul2)
