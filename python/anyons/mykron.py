class Kron():
	def __init__(self, init):
		# a and b are not hashable
		self.vect = init
	def __getitem__(self,key):
		akey = key[0]
		bkey = key[1]
		return sum( map(lambda amp,a,b: amp * a[akey] * b[bkey], self.vect))
	def bimap(self,f,g):
	#return new one or mutate self?
		return Kron(map(lambda amp,a,b: (amp, f(a), g(b)) ,self.vect))
	def lapply(self, op):
		# op is of form [(amp, f, g) ]
		return Kron(map(lambda amp,f,g: self.bimap(f,g).scalarmult(amp) ,op))
	def scalarmult(self, amp):
		return Kron(map(lambda amp1,a,b: (amp1*amp,a,b), self.vect))
	# maybe a tighter implementation is to define just lapply and define scalarmult and bimap as subcases.
	# the op form is another kron.

	# then lapply is signature Kron (a->b) (c->d) -> Kron a c -> Kron b d 
	# if we parametize amplitude type
	# Kron amp (a->b) (c->d) -> Kron amp a c -> Kron amp b d  
	# (a->b) should actually have a linear operator type (a -> Vect b)