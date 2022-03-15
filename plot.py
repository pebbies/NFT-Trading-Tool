import re
import pandas as pd
import matplotlib.pyplot as plt

data = dict()
projects = set()

with open("C:\\Users\\Stone\\Desktop\\ojbk_2\\watchlist.csv", 'r') as f:
    for line in f.readlines():
        index, project_name, date, floor_price = line.split(',')
        
        floor_price = floor_price.strip()

        if project_name not in projects:
            projects.add(project_name)

        if date not in data:
            data[project_name] = []
        data[project_name].append((date, float(floor_price)))

positions = []
for i in range(len(projects)):
    positions.append([4,4,i+1])

for i, j in enumerate(data.keys()):
    plt.subplots_adjust(top=0.95, bottom= 0.1, hspace=0.3, wspace = 0.25)
    plt.subplot(positions[i][0], positions[i][1], positions[i][2])
    data_i = dict(data[j])
    plt.bar(data_i.keys(), data_i.values())
    plt.title(j)

plt.show()