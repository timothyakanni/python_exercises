# Unique Character ---Done

import sys

data = []
with open("uniques_in.txt", "r", encoding="utf-8") as infile:
  for line in infile:
      for ch in line.strip():
          if(ch!=" " and ch not in data):
            data.append(ch)

print(data)
print()

#with open("uniques_out.txt", "w", encoding="utf-8") as outfile:
print(" ".join(data), end="\n")

