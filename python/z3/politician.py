from z3 import *

politicians = [ Bool('x%s' % i) for i in range(100) ]
#True is an honest politicians#false is a crooked one
atleastonehonest = Or(politicians)

forall2atleastonecrooked = And([ Or(Not(i), Not(j)) for i in politicians for j in politicians if not i is j])

#sol, something = solve(forall2atleastonecrooked,atleastonehonest)
s = Solver()
s.add(forall2atleastonecrooked,atleastonehonest)
#print(s.check())
s.check()
solution = s.model()
#print dir(solution[0])
#print solution
#print map(solution)
#print is_true(solution[0])
#print bool(solution[0])
solbool = [solution[pol] for pol in politicians]
print "honest men:", len([x for x in solbool if x ])
