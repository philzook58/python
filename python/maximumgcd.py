#@profile
def maximumGcdAndSum(A, B):
    if len(A) > len(B): #slight efficiency gain if A is always less than B
        temp = A
        A = B
        B = temp
    
    divsA = {}
    divsB = {}
    for a in A:
        for div in range(1, int(a**0.5)+2): # Find all divisors and place them in hash tables 
        
            if a % div == 0:
                divsA[a/div] = True
                divsA[div] = True
    for b in B:
        for div in range(1, int(b**0.5)+2):
        
            if b % div == 0:
                divsB[b/div] = True
                divsB[div] = True
    for div in sorted(divsA.keys(), reverse = True): #look at maximal divisors first, 
        if div in divsB: #fast lookup in divsB
            return max(filter(lambda x: x % div == 0,A)) + max(filter(lambda x: x % div == 0, B))

import numpy.random as random
A = np.random.randint(1,10e6, size=5e5)
B = np.random.randint(1,10e6, size=5e5)

print(maximumGcdAndSum(A,B))