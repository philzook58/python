import numpy as np

Nx = 10
Ny = 10
# store Z2 configurations on grid
# as phi[x pos ,y pos , horizontal/vertical]

nullphi = np.ones((Nx,Ny,2))

def flip(x,y,d,phi):
    phi2 = np.copy(phi)
    phi2[x,y,d] = -1 * phi2[x,y,d]
    return phi2


def flipOp(x,y,d):
    return lambda phi: flip(x,y,d,phi)

#flip00x = lambda phi: flip(0,0,0,phi)
#print flip00x(nullphi)
flip00x = flipOp(0,0,0)



#Use the notion
#Vectors are tuples of (amplitude, phi)

#take classical operation and lift it to quantum operation (conserving amplitudes)

def lift(classical_field_op):
    return lambda phi: [(1,classical_field_op(phi) )]

def extractfield(ampltiudetuple):
    return ampltiudetuple[1]
def extractamp(ampltiudetuple):
    return ampltiudetuple[0]

quantflip00x = lift(flip00x)

#Classical ground state
ground = [(1. , nullphi)]

def sigmaz(x,y,d):
    def op(phi):
        if phi[x,y,d] == 1:
            return [(1, phi)]
        elif phi[x,y,d] == -1:
            return [(-1, phi)]
    return op

def sigmax(x,y,d):
     return lift(flipOp(x,y,d))




def bind(vec,classical_op_to_vec):
    retvec = []
    for term in vec:
        phi = extractfield(term)
        amp = extractamp(term)
        newvec = classical_op_to_vec(phi)
        newvec = map(lambda (amp2,phi2): (amp2*amp,phi2) , newvec)
        retvec.extend(newvec)
    return retvec

v1 = bind(ground, quantflip00x)
v2 = bind(v1, sigmaz(0,0,0))
v3 = bind(v2, quantflip00x)

'''
print ground
print v1
print v2
print v3
'''

def toroid_my_edges(edges):
    for edge in edges:
        if edge[0] >= Nx:
            edge[0] = 0
        if edge[1] >= Ny:
            edge[1] = 0
        if edge[0] < 0:
            edge[0] = Nx-1+edge[0]
        if edge[1] < 0:
            edge[1] = Ny-1+edge[1]
    return edges


def loopedges(x,y):

    edges = [
    [x,y,0],
    [x,y,1],
    [x+1,y,1],
    [x,y+1,0]
     ]
    edges = toroid_my_edges(edges)
    return edges

def vertexedges(x,y):
    edges = [
    [x,y,0],
    [x,y,1],
    [x-1,y,0],
    [x,y-1,1]
     ]
    edges = toroid_my_edges(edges)
    return edges

#Loop and Vertex Flux ops.

'''
def Loop(x,y):
    edges = loopedges(x,y)
    def loop(phi):
        edge = loopedges[0]
        vec = sigmaz(edge[0],edge[1],edge[2])(phi)
        for edge in loopedges[1:]:
            vec = bind(vec, sigmaz(edge[0],edge[1],edge[2]))
        return vec
    return loop
'''

'''
#This version takes vec and outputs vec. More natural than one that requires a bind
def Loop(x,y):
    edges = loopedges(x,y)
    def loop(vec):
        vec = np.copy(vec)
        for edge in loopedges:
            vec = bind(vec, sigmaz(edge[0],edge[1],edge[2]))
        return vec
    return loop
    '''
# could clearly do some factoring here. COuld make function that given list of edges makes porudct of sigma z in all those edges

def Vertex(x,y):
    edges = vertexedges(x,y)
    return SigmazProd(edges)

def Loop(x,y):
    edges = loopedges(x,y)
    return SigmazProd(edges)

#Could refactor again to pass in which sigma to use
def SigmazProd(edges):
    def prod(vec):
        #vec = np.copy(vec)
        for edge in edges:
            vec = bind(vec, sigmaz(edge[0],edge[1],edge[2]))
        return vec
    return prod

def SigmaProd(edges, sigma):
    def prod(vec):
        #vec = np.copy(vec)
        for edge in edges:
            vec = bind(vec, sigma(edge[0],edge[1],edge[2]))
        return vec
    return prod

def xVertex(x,y):
    edges = vertexedges(x,y)
    return SigmaProd(edges,sigmax)

def xLoop(x,y):
    edges = loopedges(x,y)
    return SigmaProd(edges,sigmax)

def draw(phi):
    xs = np.arange(Nx)
    ys = np.arange(Ny)
    for x in xs:
        for y in ys:
            if phi[x,y,0] == 1:
                cylinder(pos=(x,y,0), axis=(1,0,0), radius = .2, color=color.red)
            else:
                cylinder(pos=(x,y,0), axis=(1,0,0), radius = .2, color=color.blue)
            if phi[x,y,1] == 1:
                cylinder(pos=(x,y,0), axis=(0,1,0), radius = .2, color=color.red)
            else:
                cylinder(pos=(x,y,0), axis=(0,1,0), radius = .2, color=color.blue)


from visual import *
#draw(flip(0,0,0,nullphi))
#draw(xLoop(1,1)(ground)[0][1])
draw(xVertex(1,1)(ground)[0][1])
draw(xLoop(3,3)(xVertex(1,1)(ground))[0][1])


def simplify(vec):
    for term in vec:
        if 

#Very good.
#However the ground state for the toric code (closed loop gas ground state) is asuperposition of a lot of
#classical configurations. This will make this computationally unwieldy.
#I don't a priori know how to even enumerate all the classical configs.
# SOOO. the high level structure can be maintained, but the implementation of the state labelling needs to be different
