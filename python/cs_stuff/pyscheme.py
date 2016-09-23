#This is clearly ripped from that one book.
#When have you known me to put error messages in my code?
#I'm a shit programmer

def tokenize(s):
	current = ''
	tokens = []
	for c in s:
		if c.isspace():
			if len(current) > 0:
				tokens.append(current)
			current = ''
		elif c in '()':
			if len(current) > 0:
				tokens.append(current)
			current = ''
			tokens.append(c)
		else:
			current = current + c
	if len(current) > 0:
		tokens.append(current)
	return tokens



def parse(s):
	def parsetokens(tokens, inner):
		res = []
		while len(tokens) > 0:
			current = tokens.pop(0)
			if current == '(':
				res.append (parsetokens(tokens, True))
			elif current == ')':
				if inner:
					return res
				else:
					error("Unmatched close paren: " + s)
					return None
			else:
				res.append(current)
		if inner:
			error ("Unmatched open paren: " + s)
			return None
		else:
			return res
	return parsetokens(tokenize(s), False)


print parse("(+ 1 (* 2 3))")

def meval(expr, env):
	if isPrimitive(expr):
		return evalPrimitive(expr)
	elif isConditional(expr):
		return evalConditional(expr, env)
	elif isDefinition(expr):
		evalDefinition(expr, env)
	elif isName(expr):
		return evalName(expr, env)
	elif isLambda(expr):
		return evalLambda(expr, env)
	elif isApplication(expr):
		return evalApplication(expr, env)
	else:
		error ("Unknown expression type: " + str(expr))
