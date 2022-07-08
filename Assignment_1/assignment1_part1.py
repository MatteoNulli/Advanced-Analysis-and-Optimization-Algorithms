from pulp import *

x = LpVariable("x", lowBound = -10)
y = LpVariable("y", upBound = 10)
prob = LpProblem("myProblem", LpMinimize)
#obj
prob += 122*x + 143*y
#constraints
prob += 3*x + 2*y <= 10
prob += 12*x + 14*y >= -12.5
prob += 2*x + 3*y >= 3
prob += 5*x - 6*y >= -100


status = prob.solve(PULP_CBC_CMD(msg=False))


#print(LpStatus[status])
print("Optimal Solution:", "x =",value(x) ," y =",value(y))
print("Objective value:", value(prob.objective))


##indentify tight constraints 
print("Tight constraints:")

i = 0
for Cj, constr in prob.constraints.items():
    i += 1
    if constr.value() == 0:
        print(i)

if value(x) == -10:
    print("5")
if value(y) == 10:
    print("6")


#Uniqueness

#prob3
z3 = LpVariable("z3")
w3 = LpVariable("w3")
prob3 = LpProblem("myProblem3", LpMinimize)

prob3 += z3

prob3 += 122.0*(z3+value(x)) + 143.0*(w3 + value(y)) == value(prob.objective)
prob3 += 3.0*(z3+value(x)) + 2.0*(w3+value(y)) <= 10.0
prob3 += 12.0*(z3+value(x)) + 14.0*(w3+value(y)) >= -12.5
prob3 += 2.0*(z3+value(x)) + 3.0*(w3+value(y)) >= 3.0
prob3 += 5.0*(z3+value(x)) - 6.0*(w3+value(y)) >= -100.0
prob3.solve(PULP_CBC_CMD(msg=False))    

#prob4
z4 = LpVariable("z4")
w4 = LpVariable("w4")
prob4 = LpProblem("myProblem4", LpMaximize)

prob4 += z4

prob4 += 122.0*(z4+value(x)) + 143.0*(w4+value(y)) == value(prob.objective)
prob4 += 3.0*(z4+value(x)) + 2.0*(w4+value(y)) <= 10.0
prob4 += 12.0*(z4+value(x)) + 14.0*(w4+value(y)) >= -12.5
prob4 += 2.0*(z4+value(x)) + 3.0*(w4+value(y)) >= 3.0
prob4 += 5.0*(z4+value(x)) - 6.0*(w4+value(y)) >= -100.0
prob4.solve(PULP_CBC_CMD(msg=False))

#prob5
z5 = LpVariable("z5")
w5 = LpVariable("w5")
prob5 = LpProblem("myProblem5", LpMinimize)

prob5 += w5

prob5 += 122.0*(z5+value(x)) + 143.0*(w5+value(y)) == value(prob.objective)
prob5 += 3.0*(z5+value(x)) + 2.0*(w5+value(y)) <= 10.0
prob5 += 12.0*(z5+value(x)) + 14.0*(w5+value(y)) >= -12.5
prob5 += 2.0*(z5+value(x)) + 3.0*(w5+value(y)) >= 3.0
prob5 += 5.0*(z5+value(x)) - 6.0*(w5+value(y)) >= -100.0
prob5.solve(PULP_CBC_CMD(msg=False))

#prob6
z6 = LpVariable("z6")
w6 = LpVariable("w6")
prob6 = LpProblem("myProblem6", LpMaximize)

prob6 += w6

prob6 += 122.0*(z6+value(x)) + 143.0*(w6+value(y)) == value(prob.objective)
prob6 += 3.0*(z6+value(x)) + 2.0*(w6+value(y)) <= 10.0
prob6 += 12.0*(z6+value(x)) + 14.0*(w6+value(y)) >= -12.5
prob6 += 2.0*(z6+value(x)) + 3.0*(w6+value(y)) >= 3.0
prob6 += 5.0*(z6+value(x)) - 6.0*(w6+value(y)) >= -100.0
prob6.solve(PULP_CBC_CMD(msg=False))


if value(z3)== 0 and value(z4) == 0 and value(w5) == 0 and value(w6) == 0:
    print("Unique optimal solution: Yes")
else:
    print("Unique optimal solution: No")

