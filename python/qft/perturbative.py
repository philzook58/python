import numpy as np


#The green's function
def G0():

#Lagrangian or Hamiltonania. Quadratic perturbstive splitting

# Very straightforward. But somehow feels inelegant to build all of this apparatus

# Generate a list of operators

# A list of operators

#Wick expander into sum of graphs

#We need a graph object. Each line is a green's function.

# a generator of graph objects up to N order

# Resummation? Recognize seqeunce of subgraphs? Similarities between previous stages and next stages?

def convertTo(vec,basis):

{comp:np.zeros(3) ,'basis':'x'}

#What is a a basis except a definition on how to transform to and from it.
#Maintain a basis graph. With calculated cost, can traverse in minimally computationally expensive way


'psi psi psi psi'

'psi(psi(psi()))'


class Symbol:
    def __init__(name):
        self.label = name

psi = Symbol("psi")

class Op:
    def __init__(name, leaf1=None,leaf2=None):
        self.label=name
        self.leaf1 = leaf1
        self.leaf2 = leaf2

root = Symbol('root')
mul = Symbol('mul', psi, psi)

def traversePrint(tree):
    print self.label
    if type(tree)== Op:
        traverse(tree.leaf1)
        traverse(tree.leaf2)
    elif type(tree) == Symbol:

traversePrint(mul)
