import networkx as nx
import numpy as np
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
    l.append(np.array(q))
#normalizing
s_10 = 0
s_others = 0
for el10, el0 in zip(l[9], l[0]):
    for p, q in zip(el10, el0):
        s_10 = p + s_10
        s_others += q

for i in range(0, 12):
    if i == 9:
        continue
    l[i] = l[i] * s_10

l[9] = l[9] * s_others

#creating graphs, adding nodes

G1 = nx.Graph()
for i in range(len(l[0])):
    for j in range(len(l[0][0])):
        t = ("1", i, j)
        G1.add_node(t, demand=-l[0][i][j])

G = []
G.append(G1)

for i in range(2, 13):
    x = nx.Graph()
    for j in range(len(l[0])):
        for h in range(len(l[0][0])):
            t = (f"{i}", j, h)
            x.add_node(t, demand=l[i-1][j][h])
    G.append(x)

column = [0 for i in range(1, 13)]

for h in range(0,12):
    for i in G[h].nodes.data():
        for j in list(i[1].values()):
            if j != 0:
                column[h] = i[0][2]

#merging graphs, adding nodes
Gm = []
for i in range(1,12):
    x = nx.DiGraph()
    x.add_nodes_from(G[0].nodes.data())
    x.add_nodes_from(G[i].nodes.data())
    Gm.append(x)

# #add edges to the graph
for i in range(0, 11):
    for j in Gm[i].nodes.data():
        for h in Gm[i].nodes.data():
            for m in list(j[1].values()):
                for n in list(h[1].values()):
                    if m != 0 and n != 0:
                        Gm[i].add_edge(j[0], h[0], weight= (column[i+1] - column[0])%80)

f_l = []
f = (0, 1)
f_l.append(f)
for i in range(0,11):
    x = (nx.min_cost_flow_cost(Gm[i]), i+2)
    f_l.append(x)

f_l.sort(key=lambda tup: tup[0])
print([f_l[i][1] for i in range(len(f_l))])
