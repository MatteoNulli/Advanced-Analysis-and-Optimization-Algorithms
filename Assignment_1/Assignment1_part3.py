from pulp import *
lpdict = LpVariable.dicts("",indices = [i for i in range (1, 70)], lowBound = 0,
                   indexStart=[], indexs=None)
prob = LpProblem("myProblem", LpMinimize)
#opening the file
our_file = open("hw1-03.txt", "r")
lplist = []
#creating a list of lists out of the file
for line in our_file:
    s_line = line.strip()
    line_list = s_line.split()
    lplist.append(line_list)
our_file.close()
#obj
prob += lpSum(lpdict)
#constraints
for vect in lplist:
    a = int(vect[0])
    b = int(vect[1])
    prob += lpdict[a] + lpdict[b]  >= 2
prob.solve(PULP_CBC_CMD(msg=False))
#print(value(prob.objective))
total = 0.0
for v in prob.variables():
    total += v.varValue
    print("representatives for company", v.name[1:], ":", v.varValue)
print("Total number of representatives involved:", total)

