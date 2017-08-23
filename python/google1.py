

mystr = "abccbaabccba"
mystr2 = "abcabc"
mystr2 = "abcabcabc"
mystr3 = "jdfkhsdjfhjsdhfjkshjfkhsdjk"
mystr4 = "qwerty"

def answer(s):
	# your code here
	# I do believe there are efficiency gains to be had
	# but this is dead simple
	N = len(s)
	# only clean divisors of N are possibilites
	factors = [x for x in range(1,N) if N % x == 0]
	for factor in factors:
		if all(s[i] == s[i + factor*j] for i in range(factor) for j in range(1,N/factor)):
			return N/factor
	return 1


print answer(mystr3)
print answer(mystr4)
print answer(mystr2)
print answer(mystr)





