import numpy as np
#This is a class that will index wraparound style, which is quite useful.
class TorusField():
    def __init__(self,initfield):
        self.field = initfield
    def __getitem__(self,index):
        x,y = self.loopIndex(index)
        return self.field[y][x]
    def loopIndex(self,index):
        y = index[1] % len(self.field)
        x = index[0] % len(self.field[0])
        return (x,y)

a = TorusField([[1,2,3],[4,5,6]])
print a[3,1]


class S3Group:
    def __init__(self,el=[1,2,3]):
        self.el = el
    def __mul__(self,other):
        perm = [0,0,0]
        for i in range(3):
            perm[i] = self.el[other.el[i]-1]
        return S3Group(el=perm)
    def __str__(self):
        return str(self.el)
    def inv(self):
        temp = [0,0,0]
        for i in range(3):
            temp[self.el[i]]=i+1
        return S3Group(temp)
    def __pow__(self,exp):
        if exp > 0:
            temp = S3Group()
            for i in range(exp):
                temp = temp * self
            return temp
        if exp == 0:
            return S3Group()
        if exp < 0:
            return self.inv() ** (-1 * exp)


print S3Group([2,1,3])
print S3Group([2,1,3]) * S3Group([2,1,3])
print S3Group() * S3Group([3,1,2])
print S3Group() * S3Group([3,1,2]) * S3Group([3,1,2])
print S3Group([2,1,3]) ** 2


Nx = 2
Ny = 2

phi = []
for i in range(Nx):
    phi.append([])
    for j in range(Ny):
        phi[i].insert(j,S3Group())

print phi

phi  = np.array(phi)

print phi
