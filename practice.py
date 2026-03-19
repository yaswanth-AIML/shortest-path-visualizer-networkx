#   tk.input_user1()
#         h=tk.h
#         G=nx.graph
#         path = nx.dijkstra_path(G, source="1", target="4")
#         length = nx.dijkstra_path_length(G, source="1", target="4")

#         print("Shortest path:", path)
#         print("Path length:", length)

#         # Layout
#         pos = nx.spring_layout(G)

#         # Draw all nodes and edges
#         nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")

#         # Draw edge weights
#         labels = nx.get_edge_attributes(G, 'weight')
#         nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

#         # Highlight the shortest path
#         path_edges = list(zip(path, path[1:]))
#         nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

#         plt.show()