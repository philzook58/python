#from sympy import Symbol
from sympy import *
psi = Symbol('psi', commutative=False)
#print psi
#print dir(psi)
#Too much.
from sympy import *
a = IndexedBase('a')
a.is_commutative=False
a._assumptions = {'commutative':False}
adag = IndexedBase('adag')
adag._assumptions = {'commutative':False}
d = IndexedBase('d')
adag.is_commutative=False
i, j = symbols('i j', cls=Idx)
ket = Symbol('|0>', commutative=False)
bra = Symbol('<0|', commutative=False)

x = Wild('x')
y = Wild('y')
expr = bra * a[i] * a[i] * a[i] * adag[i]  *adag[i] * adag[i] * ket
print expr
rules = [(a[x] * adag[y], adag[y] * a[x] + d[i,j]), (a[x] * ket, 0), (bra*adag[x], 0), (bra * ket, 1)]
expr22 =  expr.subs(rules).expand()

for i in range(10):
    expr22 = expr22.expand()
    expr22 = expr22.subs(rules)

print expr22

#I should traverse the tree by hand
#Also look into the index stuff
