


#given string find all permutations

#permute all substrings
#

#fix one, permute rest iterate

# split into two, permute two and permute within
#Nope. That is dumb. I need to do that for all sepeartions in two groups
def permute(a):

	alen = len(a)
	if alen == 1:
		return [a]
	elif alen == 0:
		return []
	split = alen//2
	permuteleft = permute(a[0:split])
	permuteright = permute(a[split:])
	permutelist = []
	for a in permuteleft:
		for b in permuteright:
			permutelist.append(a + b)
			permutelist.append(b + a)
	return permutelist

def fact(n):
	if n == 0:
		return 1
	return n * fact(n-1)
#print permute("butom")
#print fact(len("butom"))
#assert len(permute("butom")) == fact(len("butom"))


def permute2(a):
	permutes = []
	for i in range(len(a)):
		lesserpermutes = permute2(a[:i] + a[i+1:]		
		permutes = permutes + map(lambda x: i + x, lesserpermutes)
	return permutes



mystr = "bezlt"
permute2(mystr)


