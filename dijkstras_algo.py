import networkx as nx
import matplotlib.pyplot as plt

def run_dijkstra(h, source, target):
    G = nx.Graph()
    G.add_weighted_edges_from(h)
    try:
        path = nx.dijkstra_path(G, source=source, target=target)
        length = nx.dijkstra_path_length(G, source=source, target=target)
        print("Shortest path:", path)
        print("Path length:", length)
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G, pos, node_color="lightblue")
        nx.draw_networkx_edges(G, pos, edge_color="gray")
        nx.draw_networkx_labels(G, pos)
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
        plt.show()
    except nx.NetworkXNoPath:
        print(f"No path exists between {source} and {target}.")