
# I should build an interpreter.
# THEN use interpeter to do concurrency stuff
# garbage collection

#Question? Do I bother parsing?



program1 = ["define", "square" , ['lambda', ["x"], ["*","x","x"]]] #Fairly unreadable It's the quotation marks mostly.

program2 = [['lambda', ["x"], ["*","x","x"]], "3"] 

program3 = "[yada yada  ]" # could process on this to 
#options:
x = "x" #This is similar to listing out possible keywords anyway
# not going to be able to do *. Maybe instead mult
mult = "mult"
add = "add"
define = "define"
lam = "lambda"

program4 = [define, "square", [lam, [x], [mult, x, x]]]
#That's not bad
# doing everything as strings sucks though
#could match on explicit keywords easily and everything else is whatev
# also could check type
if type(3) == int:
	print "yeaaaaaaah"
if type(True) = bool:
	print "buddddddyyy"

if l[0] == mult:
	return reduce(lambda x,y: x*y, l[1:])
#class Expr:
#class Lambda:

program5 = [mult, 3, 3]


eval("x = 'x' " )

#maybe this is a good use case for a macro
# some like program4 = Program([  ]) and then it quotes around every subexpress to string them


put(name):
	eval(name + " = \"" + name + "\""   ) #This function would put name in current context if it weren't for funciton scoping
