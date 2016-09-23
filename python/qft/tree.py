
class Node:
    def __init__(self, label, leaves=[],data=None):
        self.label = label
        self.leaves = leaves
        self.data = data
    def __mul__(self,other):
        return Node('*', leaves=[self,other])
    def __add__(self,other):
        return Node('+', leaves=[self,other])
    def __str__(self):
        if self.leaves == []:
            return self.label
        else:
            return '(' + self.label + ' ' + ' '.join(str(p) for p in self.leaves)  + ')'

a_i = Node('a',data='i')
adag_j = Node('adag',data='j')

mul = Node('*', leaves=[a_i, adag_j])
print mul

print a_i * adag_j + a_i * a_i

def replace(tree, pattern, new):
