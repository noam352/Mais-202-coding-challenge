"""
Noam Cohen U1
MAIS 202 coding challenge

"""


import matplotlib.pyplot as plt
import numpy as np
import plotly    
import plotly.graph_objs as go.    ## used at the bottom of the code



file=open('data.csv','r')               ## file stream variable
line = file.readline()
array_lines=[]
array_lines.append(line)                ##array where each entry is a line from the stream

while line:
    line=file.readline()
    array_lines.append(line)
    
file.close()
                                        ## initialising my arrays where i will store data
purpose_array=[]                        ## array that contaisn the purposes as trings
rate_2d_array=[[]]                      ## 2d array where each sub array is the list ofrates that belong to the same purpose (matching indexs)
average_array=[]                        ## average rate of each sub array
array_lines.pop()                       ## ignores the last line of the file

for count,line in enumerate(array_lines):
    x=0
    
    if (count == 0 ): ##for table headers
        continue
    
    for i in range (5):
        x=line.index(',')
        line=line[x+1:]

    end_index=line.index(',')
    rate=line[:end_index]
    
    for i in range(11):
        x=line.index(',')
        line=line[x+1:]

    end_index2=line.index(',')
    temp_string=line[:end_index2]
    
    if ((temp_string in purpose_array) == False):
        purpose_array.append(temp_string)

    purpose_index=purpose_array.index(temp_string)
    
    if (purpose_index==len(rate_2d_array) and purpose_index!=0):
        rate_2d_array.append([rate])
    else:    
        rate_2d_array[purpose_index].append(rate)
    
for i in rate_2d_array:
    cur_average=0.0
    for p in i:
        cur_average+=float(p)
    cur_average/=float(len(i))
    average_array.append(cur_average)


##print(rate_2d_array)
##print(purpose_array)
##print(average_array)




x = np.arange(len(purpose_array))
fig, ax = plt.subplots()
plt.bar(x,average_array)
plt.xticks(x,(i for i in purpose_array))
plt.show()


trace = go.Table(                                                       ## My experience using plotlys library!!!
    header=dict(values=[' ', 'purpose', 'avg_rate']),
    cells=dict(values=[ [i for i in range(len(purpose_array))],
                       purpose_array, average_array],
               align = ['left']
               )
                )

layout = dict(width=500, height=2000)
data = [trace]
fig2 = dict(data=data, layout=layout)
plotly.offline.plot(fig2, filename = 'basic_table.html')

