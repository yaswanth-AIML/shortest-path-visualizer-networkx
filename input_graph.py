import networkx as nx
import matplotlib.pyplot as plt
h=[]
def input_user():
    while True:
        try:
            num=int(input("Enter The Total Number Of Edges: "))
            weightone=input("Do You Wanna Enter Weight YES or NO :")
            if weightone.lower()=="yes":
                k=0
            elif weightone.lower()=="no":
                k=2
            else:
                print("ENTER THE CORRECT CHOICE")
        except:
            print("'ENTER THE NUMBER'")
        else:
            for i in range(1,num+1):
                verter1=input(f"Enter Vertex 1 for Edge {i}: ")
                vertex2=input(f"Enter Vertex 2 for Edge {i}: ")
                if k==0:
                    try:
                        weight=int(input("Add The Weight Also: "))
                    except:
                        print("ENTER THE NUMBER FOR WEIGHT")
                    else:
                        h.append((verter1,vertex2,weight))
                else:
                    h.append((verter1,vertex2))
            print(h)
            try:
                layout_input=int(input(("In Which Way You Wanna Visuvalize The Graph\n" \
                "1 for Spring_layout\n" \
                "2 for circular_layout\n" \
                "3 for random_layout\n" \
                "4 for planar_layout\n" \
                "ENTER:")))
            except:
                print("ENTER NUMBER ONLY")
            else:
                g=nx.Graph()
                if k==0:
                    g.add_weighted_edges_from(h)
                else:
                    g.add_edges_from(h)
                if layout_input==1:
                    layout=nx.spring_layout(g)
                elif layout_input==2:
                    layout=nx.circular_layout(g)
                elif layout_input==3:
                    layout=nx.random_layout(g)
                elif layout_input==4:
                    layout=nx.planar_layout(g)
                else:
                    print("ENTER THE CORRECT NUMBER:")
                    layout=nx.spring_layout(g)
                if k==0:
                    g.add_weighted_edges_from(h)
                    pos = layout#layout part
                    nx.draw(g, pos, with_labels=True)
                    labels = nx.get_edge_attributes(g,'weight')
                    nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
                    break
                else:
                    g.add_edges_from(h)
                    pos=layout
                    nx.draw(g,pos,with_labels=True)
                    plt.show()
                    break
def input_user1():
    while True:
        try:
            num=int(input("Enter The Total Number Of Edges: "))
        except:
            print("'ENTER THE NUMBER'")
        else:
            for i in range(1,num+1):
                verter1=input(f"Enter Vertex 1 for Edge {i}: ")
                vertex2=input(f"Enter Vertex 2 for Edge {i}: ")
                try:
                    weight=int(input("Add The Weight Also: "))
                except:
                    print("ENTER THE NUMBER FOR WEIGHT")
                else:
                    h.append((verter1,vertex2,weight))
            print(h)
            # g=nx.Graph()
            # g.add_weighted_edges_from(h)
            # pos = nx.spring_layout(g)
            # nx.draw(g, pos, with_labels=True)
            # labels = nx.get_edge_attributes(g,'weight')
            # nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
            #break
# g=nx.Graph()
# nx.draw_spring(g,with_labels=True)
# plt.show()
# nx.draw_random(g,with_labels=True)
# plt.show()
# import networkx as nx
# import matplotlib.pyplot as plt
# h=[]
# num=int(input("Enter The Total Number Of Edges: "))
# for i in range(1,num+1):
#     vertex1=input(f"Enter Vertex 1 for Edge {i}: ")
#     vertex2=input(f"Enter Vertex 2 for Edge {i}: ")
#     weight=int(input("Add The Weight Also: "))
#     h.append((vertex1,vertex2,weight))
# print(h)
# g=nx.Graph()
# g.add_weighted_edges_from(h)
# pos = nx.spring_layout(g)
# nx.draw(g, pos, with_labels=True)
# labels = nx.get_edge_attributes(g,'weight')
# nx.draw_networkx_edge_labels(g, pos, edge_labels=labels)
# plt.show()