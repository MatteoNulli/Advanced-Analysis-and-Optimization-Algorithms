from pulp import *

x1 = LpVariable("x1", 0,1)
x2 = LpVariable("x2", 0,1)
x3 = LpVariable("x3", 0,1)
x4 = LpVariable("x4", 0,1)
x5 = LpVariable("x5", 0,1)
x6 = LpVariable("x6", 0,1)

x0 = LpVariable("x0", lowBound = None, upBound = None) 

prob = LpProblem("myProblem", LpMaximize)
#obj
prob += x0
#constraints
prob += x0 <= -2*x2 + x3 + x4 + x5 + x6
prob += x0 <=  +2*x1 + -2*x3 + x4 + x5 + x6
prob += x0 <= -1*x1 + +2*x2 + -2*x4 + x5 + x6
prob += x0 <= -1*x1 + -1*x2 + +2*x3 + -2*x5 + x6
prob += x0 <= -1*x1 + -1*x2 + -1*x3 + +2*x4 + -2*x6
prob += x0 <=  -1*x1 + -1*x2 + -1*x3 + -1*x4 + +2*x5
prob += x1 + x2 + x3 + x4 + x5 + x6 == 1

prob.solve(PULP_CBC_CMD(msg=False))


for var in prob.variables()[1:]:
    print(var.name, ":", var.value())
    
    




