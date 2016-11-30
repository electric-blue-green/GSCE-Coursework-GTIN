import re

change = input('Enter change here: ')
line = input('Enter Cell Line (Py +1): ')
column = input('Enter Cell Column (Py+1): ')
change = str(change)
line = int(line)
column = int(column)

data = open("test.csv").read()
data = data.split("\n")
for i, s in enumerate(data):
  data[i] = data[i].split(",")
  
data[line][column] = change

for i, s in enumerate(data):
  data[i] = ",".join(data[i])
data = "\n".join(data)
o = open("test.csv","w")
o.write(data)
o.close()
