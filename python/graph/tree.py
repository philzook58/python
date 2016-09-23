import networkx as nx
import matplotlib.pyplot as plt

T=nx.DiGraph()


N=11
T.add_nodes_from(range(6))

T.add_edges_from(zip( range(0,N,2), range(1,N,2)))
T.add_edges_from(zip( range(0,N-1,2), range(2,N,2)))

print T.edges()




assert nx.is_tree(T)

nx.draw(T)
#nx.draw_spectral(T)
plt.show()