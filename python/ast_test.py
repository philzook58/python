import ast

f = open('clebsch.py','r')
tree = ast.parse(f.read())


tree = ast.parse("print 'Hello World'")
exec(compile(tree, filename="<ast>", mode="exec"))


print ast.dump(tree)