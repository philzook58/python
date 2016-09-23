#from sympy import Symbol
from sympy import *
psi = Symbol('psi', commuative=False)
#print psi
#print dir(psi)
#Too much.
from sympy import *
a = Symbol('a', commutative=False)
adag = Symbol('adag', commutative=False)
ket = Symbol('|0>', commutative=False)
bra = Symbol('<0|', commutative=False)

expr = bra * a * a * a * adag  *adag * adag * ket
print expr
rules = [(a * adag, adag * a + 1), (a * ket, 0), (bra*adag, 0), (bra * ket, 1)]
expr22 =  expr.subs([(a * adag, adag * a + 1), (a * ket, 0), (bra*adag, 0), (bra * ket, 1)]).expand()

for i in range(10):
    expr22 = expr22.expand()
    expr22 = expr22.subs(rules)
print expr22

#I should traverse the tree by hand
#Also look into the index stuff
