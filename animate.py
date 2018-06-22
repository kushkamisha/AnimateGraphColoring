import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# generate graph
A = np.matrix([
    [1,0,0,0,1],
    [0,1,1,1,0],
    [0,1,1,0,1],
    [0,1,0,1,1],
    [1,0,1,1,1]
])
G = nx.from_numpy_matrix(A)

# explicitly set positions of nodes
pos = {0: (0, 1),
       1: (3, 1),
       2: (2, 2),
       3: (2, 0),
       4: (1, 1)}


# generating input frames
frame = np.array([
    [0, 0, 1, 1, 2],
    [0, 0, 1, 2, 1],
    [0, 0, 1, 1, 2],
    [0, 0, 2, 1, 1],
    [0, 0, 1, 1, 2],
    [2, 0, 1, 1, 0],
    [1, 0, 1, 1, 0],
])

# number of nodes
size = len(frame)

# draw the topology of the graph, what changes during animation
# is just the color
nodes = nx.draw_networkx_nodes(G, pos, node_size=500,)
edges = nx.draw_networkx_edges(G, pos)
labels = nx.draw_networkx_labels(G, pos, font_color='w')
plt.axis('off')

# pass frames to funcanimation via update function
def update(i):
    nc = frame[i]
    nodes.set_array(nc)
    return nodes,

# save animation
fig = plt.gcf()
ani = FuncAnimation(fig, update, interval=50, frames=range(size), blit=True)
ani.save('bee_coloring.gif', writer='imagemagick',  savefig_kwargs={'facecolor':'white'}, fps=0.5)
