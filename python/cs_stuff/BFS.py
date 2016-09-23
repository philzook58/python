

frontier = []
vertices = [1,2,3,4]
parent = {}

frontier = [v[0]]
parent[v[0]] = None
while frontier != {}:
	newfrontier = []
	for v in frontier:
		for node in adj(v)
			if node not in parent:
				parent[node] = v
				frotier.append(node)
			


