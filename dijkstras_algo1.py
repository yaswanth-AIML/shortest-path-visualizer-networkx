import networkx as nx
import matplotlib.pyplot as plt

def build_graph():
    h = []
    num = int(input("Enter The Total Number Of Edges: "))
    weighted = input("Do you want to enter weights? (yes/no): ").lower()

    for i in range(1, num+1):
        v1 = input(f"Enter Vertex 1 for Edge {i}: ")
        v2 = input(f"Enter Vertex 2 for Edge {i}: ")
        if weighted == "yes":
            weight = int(input("Add The Weight Also: "))
            h.append((v1, v2, weight))
        else:
            h.append((v1, v2))

    if weighted == "yes":
        G = nx.Graph()
        G.add_weighted_edges_from(h)
    else:
        G = nx.Graph()
        G.add_edges_from(h)

    return G, weighted == "yes"

def choose_layout(G):
    print("\nChoose Layout:")
    print("1. Spring Layout")
    print("2. Circular Layout")
    print("3. Random Layout")
    print("4. Planar Layout")

    choice = int(input("Enter your choice: "))
    if choice == 1:
        return nx.spring_layout(G)
    elif choice == 2:
        return nx.circular_layout(G)
    elif choice == 3:
        return nx.random_layout(G)
    elif choice == 4:
        return nx.planar_layout(G)
    else:
        print("Invalid choice, using spring layout.")
        return nx.spring_layout(G)

def visualize_graph(G, pos, weighted):
    nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")
    if weighted:
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
    plt.show()

def run_dijkstra(G, pos):
    source = input("Enter source node: ")
    target = input("Enter target node: ")

    try:
        path = nx.dijkstra_path(G, source=source, target=target)
        length = nx.dijkstra_path_length(G, source=source, target=target)
        print("Shortest path:", path)
        print("Path length:", length)

        # Draw graph with highlighted path
        nx.draw(G, pos, with_labels=True, node_color="lightblue", edge_color="gray")
        labels = nx.get_edge_attributes(G, 'weight')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)

        path_edges = list(zip(path, path[1:]))
        nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)

        plt.show()
    except nx.NetworkXNoPath:
        print(f"No path exists between {source} and {target}.")

def main():
    print("WELCOME TO GRAPHS")
    while True:
        print("\nENTER")
        print("1 for Graph Visualization")
        print("2 for Dijkstra's Algorithm")
        print("3 for Exit")
        choice = int(input("Enter Your Choice: "))

        if choice == 1:
            G, weighted = build_graph()
            pos = choose_layout(G)
            visualize_graph(G, pos, weighted)

        elif choice == 2:
            G, weighted = build_graph()
            pos = choose_layout(G)
            run_dijkstra(G, pos)

        elif choice == 3:
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main()