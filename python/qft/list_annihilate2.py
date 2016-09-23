

class Op:
    def __init__(self,label, index=()):
        self.label=label
        self.index=index
    def __str__(self):
        return self.label +  str(self.index)


a = Op('a',('i'))
adag = Op('adag',('j'))
delta= Op('delta',('i','j'))

expr = [a,adag]
print delta


def evalexpr(expr):
    if expr == []:
        return [1]
    if expr[-1].label=='a':
        return [0]
    elif expr[0].label=='adag':
        return [0]
    else:
        for i in range(len(expr)-1):
            if expr[i].label=='a' and expr[i+1].label=='adag':
                head = expr[0:i]
                if i+2 < len(expr):
                    tail = expr[i+2:]
                else:
                    tail = []
                return
                a =  evalexpr(head+tail)
                b = evalexpr(head+[adag,a]+tail)
                if a == [0] and b==[0]:
                    return [0]
                elif a == [0]:
                     return b
                elif b == [0]:
                    return [a,Op('delta', (expr[i].index[0],expr[1+i].index[0]))]
                else:
                    return [[a,Op('delta', (expr[i].index[0],expr[1+i].index[0]))] , b]
                break

print evalexpr([a,a,a, adag, adag,adag])
