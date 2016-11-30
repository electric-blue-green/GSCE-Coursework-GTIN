import re
data = open("test.csv").read()
data = data.split("\n")
for i, s in enumerate(data):
  data[i] = data[i].split(",")
  
data[1][1] = "NEON ORANGE PAINT"

for i, s in enumerate(data):
  data[i] = ",".join(data[i])
data = "\n".join(data)
o = open("test.csv","w")
o.write(data)
o.close()
