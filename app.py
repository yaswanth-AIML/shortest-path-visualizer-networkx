from flask import Flask, render_template, request
import matplotlib.pyplot as plt
import networkx as nx

app = Flask(__name__)
@app.route("/", methods=["GET", "POST"])
def index():
    path = None
    length = None
    img_path = None
    if request.method == "POST":
        mode = request.form["mode"]
        edges_input = request.form["edges"]
        layout_choice = request.form["layout"]
        edges = []
        lines = edges_input.strip().split("\n")
        for line in lines:
            parts = line.split()
            if len(parts) == 3:
                edges.append((parts[0], parts[1], int(parts[2])))
            elif len(parts) == 2:
                edges.append((parts[0], parts[1]))
        G = nx.Graph()
        weighted = any(len(e) == 3 for e in edges)
        if weighted:
            G.add_weighted_edges_from([e for e in edges if len(e) == 3])
        else:
            G.add_edges_from(edges)
        if layout_choice == "spring":
            pos = nx.spring_layout(G)
        elif layout_choice == "circular":
            pos = nx.circular_layout(G)
        elif layout_choice == "random":
            pos = nx.random_layout(G)
        else:
            try:
                pos = nx.planar_layout(G)
            except:
                pos = nx.spring_layout(G)
        plt.figure(figsize=(6,6))
        nx.draw(G, pos, with_labels=True, node_color="lightblue")
        if weighted:
            labels = nx.get_edge_attributes(G, 'weight')
            nx.draw_networkx_edge_labels(G, pos, edge_labels=labels)
        if mode == "dijkstra":
            source = request.form["source"]
            target = request.form["target"]
            try:
                path = nx.dijkstra_path(G, source, target)
                length = nx.dijkstra_path_length(G, source, target)

                path_edges = list(zip(path, path[1:]))
                nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=3)
            except:
                path = "No path found"
                length = "-"
        img_path = "static/graph.png"
        plt.savefig(img_path)
        plt.close()
    return render_template("index.html", path=path, length=length, img_path=img_path)
if __name__ == "__main__":
    app.run(debug=True)