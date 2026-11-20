from skimage import io
from skan import Skeleton, summarize
import matplotlib.pyplot as plt
import networkx as nx


# Gespeichertes Skelett einlesen
image = io.imread('../bilder/skeleton.png', as_gray=True)
binary = image > 0.5
graph = Skeleton(binary)
branches = summarize(graph, separator='_')

positions = {}
G = nx.Graph()
for i in range(branches.shape[0]):
    coords = graph.path_coordinates(i)

    # Skan liefert (y, x)
    y = coords[:, 0]
    x = coords[:, 1]

    # Start- und Endpunkt bestimmen
    start = (x[0], y[0])
    end = (x[-1], y[-1])

    # Positionen speichern
    positions[str(i * 2)] = start
    positions[str(i * 2 + 1)] = end

    # Kante hinzufügen
    G.add_edge(
        str(i * 2),
        str(i * 2 + 1),
        label=str(i * 2)
    )

nx.draw_networkx_nodes(G, pos=positions, node_size=500)
nx.draw_networkx_edges(G, pos=positions, edgelist=G.edges(), edge_color='black', arrows=True)
plt.gca().invert_yaxis()
plt.axis("equal")
plt.show()