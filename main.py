import input_graph as tk
import dijkstras_algo as dk
print("WELCOME TO GRAPHS")
while True:
    try:
        num=int(input("ENTER \n"
        "1 for graph visuvalization\n" \
        "2 for dijkstras algorithm\n" \
        "3 for Exit\n"\
        "Enter Your Choice:"))
    except:
        print("ENTER NUMBER ONLY")
        continue
    if num==1:
        tk.input_user()
        h=tk.h
        h.clear()
    elif num==2:
        tk.input_user1()
        h=tk.h
        source=input("Enter source Point:")
        target=input("enter target point :")
        dk.run_dijkstra(h,source,target)
        h.clear()
    elif num==3:
        quit()
    else:
        print("ENTER 1 OR 2 ONLY")