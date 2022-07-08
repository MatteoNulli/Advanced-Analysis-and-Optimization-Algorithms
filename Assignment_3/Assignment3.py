from pulp import *
import numpy as np
import pandas as pd
import datetime
import plotly.figure_factory as ff

#open the file using numpy
bak_f = np.genfromtxt('bakery.txt', dtype=int)

#creating lists for notational purposes
pre = bak_f[:, 1]
dln = bak_f[:, 2]
bak_time = bak_f[:, 3]

M = max(dln) + 1

#define the Linear Programm

prob = LpProblem("LpProblem", LpMinimize)
#e_max represents the maximum ending time
e_max = LpVariable("max_ending_time")

#dict of starting times denoting when should each pastry be put into oven
s = LpVariable.dicts("s_times", indices= [i for i in range(len(pre))], cat = "Integer")

#binary variable, switching on and off the "ei ≤ sj or ej ≤ si" constraints accordingly
z = LpVariable.dicts("bin_var", indices= [(i,j) for i in range(len(pre)) for j in range(len(pre))], cat="Binary")

#adding the objective to the problem
prob += e_max

#adding the constraints
for i in range(len(s)):
    #each starting time should be >= then the time since midnight since when the pastry is ready for baking
    prob += s[i] >= pre[i]

    #the time when the pastry can be put in the oven + the baking time of the pastry <= deadline_i
    prob += s[i] + bak_time[i] <= dln[i]

    # this is the maximum ending time e_max >= all other ending times e_i
    prob += e_max >= s[i] + bak_time[i]
    #now apply the bigM method switching off constraints
    for j in range(len(s)):
        if i != j:
            prob += s[i] + bak_time[i] <= s[j] + (M * z[i, j])
            prob += s[j] + bak_time[j] <= s[i] + (M * (1 - z[i, j]))

#the maximum ending time should be no more then the maximum deadline
prob += e_max <= max(dln)

status = prob.solve(PULP_CBC_CMD(msg=False))

##DELETE THIS
#print(value(e_max))

#printing List of starting times of each pastry
for i in range(len(s)):
    print(f"s{i}: {s[i].varValue}")


#visualizing the solution

s_l = [s[i].varValue for i in range(len(pre))]
#transforming dln column into list
dln_list = dln.tolist()

#creating an empty pandas data frame
df_n = pd.DataFrame()

#define the Super Critical Condition and Critical Conditions to be those pastries whose late start
#would delay mostly the others.
#Super Critical Condition is gap between when the pastry is put into the oven and when it is ready = 0,
#Critical Condition is gap between when the pastry is put into the oven and when it is ready <= 30 minutes,
#Normal Condition is gap between when the pastry is put into the oven and when it is ready > 30 minutes,

#we set a time of 30 minutes as benchmark (we could have chosen a different time).

for i in range(len(pre)):
    if s_l[i] - pre[i] == 0:
        strg = 'gap between when the pastry is put into the oven and when it is ready = 0, Super Critical Condition'
    elif s_l[i] - pre[i] <= 1800:
        strg = 'gap between when the pastry is put into the oven and when it is ready <= 30 minutes, Critical Condition'
    elif s_l[i] - pre[i] > 1800:
        strg = 'gap between when the pastry is put into the oven and when it is ready > 30 minutes, Normal Condition'
    starting_date = datetime.timedelta(seconds = s_l[i])
    finishing_date = datetime.timedelta(seconds = (s_l[i] + bak_time[i]))
    el = dict(Task=f"Pastry{i}", Start='2022-04-02 %s' %(starting_date),
              Finish='2022-04-02 %s' %(finishing_date), Resource = strg)
    df_n = df_n.append(el, ignore_index=True)



colors = {'gap between when the pastry is put into the oven and when it is ready = 0, Super Critical Condition': (1, 0.1, 0.16),
          'gap between when the pastry is put into the oven and when it is ready <= 30 minutes, Critical Condition': (1, 0.8, 0.16),
          'gap between when the pastry is put into the oven and when it is ready > 30 minutes, Normal Condition': 'rgb(0, 200, 150)'}

#adding vertical Royal Blue lines representing deadlines

df_n["DLN"] = dln_list

df_n.sort_values(by=['Start'], inplace=True)

fig1 = ff.create_gantt(df_n, colors=colors, index_col='Resource',
                       show_colorbar=True, group_tasks=True)

dln_L_list = [i for i in df_n["DLN"]]


for i in range(len(dln_list)):
    dln_date = datetime.timedelta(seconds=dln_L_list[i])
    fig1.add_shape(type="line",
                    x0='2022-04-02 %s' % (dln_date), y0=15.5 - i, x1='2022-04-02 %s' % (dln_date), y1=16.5 - i,
                    line=dict(color="royalblue", width=3))


#this is optional if someone wants to see the final figure
fig1.show()
