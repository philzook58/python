
#myfor returns a stateful computation that takes state i 
'''
def myfor(cond, myiter):
	def f(i):
		if cond(i):
			return lambda j: (val, myiter(j))
		else:
			return lambda j: (val , j)
	return f

def geti():
	return lambda j: (j,j)
'''

'''
# both push and pop take nothing to state transfromer since they don't deped on value

#currying would help correpsondence to haskell. Then push(a,stack): wuld be the same as push(a): retrun lambda stack
def push(a):
	return lambda stack: (None, [a] + stack)

def pop():
	return lambda stack:  (stack[0], stack[1:])

def myreturn(x):
	return lambda stack: (x, stack)
'''
def liftfunc(f):
	return lambda x: ( f(x) )
'''
def runStackFunc(statefulstackfunc):
	return statefulstackfunc([])

#state -> (val ,state)
def bind(statemanip, regtostatemanip):       #  retrun val  #state
	return lambda state: regtostatemanip(statemanip(state)[0])(statemanip(state)[1])

#Do notation is also pretty clutch. You need to toss the value a lot

print runStackFunc(bind(bind(push(1), lambda _ : push(2)), lambda _ :pop()))

'''




# This is horrific

#currying would help correpsondence to haskell. Then push(a,stack): wuld be the same as push(a): retrun lambda stack
def push(a):
	return lambda stack: (None, [a] + stack)


pop = lambda stack:  (stack[0], stack[1:])
def myreturn(x):
	return lambda stack: (x, stack)

def runStackFunc(statefulstackfunc):
	return statefulstackfunc([])

#state -> (val ,state)
def bind(statemanip, regtostatemanip):       #  retrun val  #state
	return lambda state: regtostatemanip(statemanip(state)[0])(statemanip(state)[1])
'''
def then(statemanip, dontneednothin):
	return lambda state: (dontneednothin(statemanip(state)[1]))
'''
#More general 
def then(statemanip, dontneednothin):
	return bind(statemanip, lambda _: dontneednothin)


#Do notation is also pretty clutch. You need to toss the value a lot

print runStackFunc(bind(bind(bind(push(1), lambda _ : push(2)), lambda __ :pop), push))
# associativity?  The valiue tssing lambdas need to be switched outside of the binds. That seems weird
print runStackFunc(bind(push(1), lambda _ :bind( push(2), lambda __: bind(pop, push))))

print runStackFunc(bind(bind(push(1), lambda _: push(2)), lambda __: bind(pop, push)))

print runStackFunc(bind(then(then(push(1), push(2)), pop), push))

