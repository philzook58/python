import heap

a = heap.PriorityQueue()

lev, leaf = a.levelleaf(20)

assert a.index(lev,leaf) == 20
lev, leaf = a.levelleaf(2)
assert lev == 1
assert leaf ==1
assert a.index(0,0) == 0
assert a.index(2,0) == 3 

a.append(3)

a.append(4)

a.append(2)

a.append(1)


a.append(4)

a.append(14)
a.append(2)
a.append(102)
a.append(-1)
a.append(2)
a.append(4)



print a.queue

a.pop()
a.pop()
a.pop()
a.pop()

print a.queue