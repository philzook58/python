import networkx as nx
G=nx.Graph()


G.add_node(1)

G.add_nodes_from([2,3])

G.add_edge(1,2)
G.add_edges_from([(1,2),(1,3)])

nx.connected_components(G)

import matplotlib.pyplot as plt

#nx.draw(G)
# nx.draw_random(G)
#nx.draw_circular(G)
#nx.draw_spectral(G)

plt.show()

# Could make a graph that associates labels with edges of particle type
# and could attach Nijk to vertices I suppose