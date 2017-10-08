# DNA Sequence ---

import sys

data = []
with open("dnainput.txt", "r") as infile:
  for line in infile:
    data.append(line.strip().split("\n"))


#with open(sys.argv[2], "w") as outfile:
for i in data:
    for j in i:
        m = (j.split(" "))
        if m[0] and m[0].isdigit():
            print("".join(m[1:]), end="\n")
        else:
            pass



