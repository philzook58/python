
'''
a = ('a',1)
adag = ('adag',1)

expr = [a,adag]
'''

def evalexpr(expr):
    if expr == []:
        return 1
    if expr[-1]=='a':
        return 0
    elif expr[0]=='adag':
        return 0
    else:
        for i in range(len(expr)-1):
            if expr[i]=='a' and expr[i+1]=='adag':
                head = expr[0:i]
                if i+2 < len(expr):
                    tail = expr[i+2:]
                else:
                    tail = []
                return evalexpr(head+tail) + evalexpr(head+['adag','a']+tail)
                break

print evalexpr(['a','a','a', 'adag', 'adag','adag'])
