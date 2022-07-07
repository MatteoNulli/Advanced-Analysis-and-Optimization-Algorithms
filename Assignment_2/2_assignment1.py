import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
import networkx as nx

#create lists
p = []
l = []

for i in range(1,13):
    x = open(f"P{i}.txt", "r")
    p.append(x)

for i in p:
    q = []
    for line in i:
        y = [int(j) for j in list(line)[:-1]]
        q.append(y)
    l.append(q)





G1 = nx.Graph()
for i in range(len(l[0])):
    for j in range(len(l[0][0])):
        t = ("1", i, j)
        G1.add_node(t, demand = -l[0][i][j])
              

G = []
G.append(G1)

for i in range(2,13):
    x = nx.Graph()
    G.append(x)
    for j in range(len(l[0])):
        for h in range(len(l[0][0])):
            t = (f"{i}",j,h)
            x.add_node(t, demand = l[i-1][j][h])


column = [100 for i in range(1,13)]
 
for h in range(0,12):
    for i in G[h].nodes.data():
        for j in list(i[1].values()):
            if j != 0:
                column[h] = i[0][2]

print(column)

#merge the two graphs 1-2
Gm = []
for i in range(1,12):
    x = nx.DiGraph()
    x.add_nodes_from(G[0].nodes.data())
    x.add_nodes_from(G[i].nodes.data())
    Gm.append(x)

# #add edges to the graph
for i in range(len(Gm)):
    for j in Gm[i].nodes.data():
        for h in Gm[i].nodes.data():
            for m in list(j[1].values()):
                for n in list(h[1].values()):
                    if m!= 0 and n!= 0:
                        Gm[i].add_edge(j[0] , h[0], weight = column[i+1] - column[0]) 


f_l = []
for i in range(0,12):
    x = (nx.min_cost_flow_cost(Gm[i]), i+2)
    f_l.append(x)
    
print(f_l)



# for i in G12.nodes.data():
#     for j in G12.nodes.data(): 
#         for k in list(i[1].values()):
#             for h in list(j[1].values()):
#                 if k!= 0 and h != 0:
#                     G12.add_edge(i[0] , j[0], weight = column2 - column1) 
                    
# #                     it does not work but basically we are using the difference between the columns
   
    

# G12.add_nodes_from(G1.nodes.data())
# G12.add_nodes_from(G2.nodes.data())

# #add edges to the graph
# for i in G12.nodes.data():
#     for j in G12.nodes.data(): 
#         for k in list(i[1].values()):
#             for h in list(j[1].values()):
#                 if k!= 0 and h != 0:
#                     G12.add_edge(i[0] , j[0], weight = column2 - column1) 
                    
# #                     it does not work but basically we are using the difference between the columns
   

# # print(G12.number_of_nodes())
# # print(G12.number_of_edges())
# print(nx.min_cost_flow_cost(G12))

                     
      


















# l1_2 = []
# for i in G1.nodes.data():
#     for j in G2.nodes.data(): 
#         for k in list(j[1].values()):
#                 s = abs(i[0][1] - j[0][1]) * k
#                 l1_2.append(s)

# dist12 = sum(l1_2)
# print(dist12)



# l1_3 = []
# for i in G1.nodes.data():
#     for j in G3.nodes.data():
#         for k in list(j[1].values()):
#                 s = (i[0][1] - j[0][1]) * k
#                 l1_3.append(s)

# dist13 = sum(l1_3)
# print(dist13)


# l1_4 = []
# for i in G1.nodes.data():
#     for j in G4.nodes.data():
#         for k in list(j[1].values()):
#                 s = (i[0][1] - j[0][1]) * k
#                 l1_4.append(s)

# dist14 = sum(l1_4)
# print(dist14)


# l1_5 = []
# for i in G1.nodes.data():
#     for j in G5.nodes.data():
#         for k in list(j[1].values()):
#                 s = (i[0][1] - j[0][1]) * k
#                 l1_5.append(s)

# dist15 = sum(l1_5)
# print(dist15)

            


