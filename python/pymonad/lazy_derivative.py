import math

def monomial(n):
	fact = 1
	for i in range(n):
		yield lambda x: fact * x**(n-i)
		fact = (n-i) * fact
	yield lambda x: fact
	while True:
		yield lambda x: 0

def constant(c):
	yield lambda x: c
	while True:
		yield lambda x: 0

def sin():
	while True:
		yield math.sin
		yield math.cos
		yield lambda x: -1 * math.sin(x)
		yield lambda x: -1 * math.cos(x)


def cos():
	msin = sin()
	next(msin)
	while True:
		yield msin.next()

def exp(x):
	while True:
		yield math.exp


def compose(f, g):
	


def mult(f,g):


def add(f,g):
