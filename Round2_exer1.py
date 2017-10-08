# Country Name in order --- Done

# Here we read file line by line
# and put the value in data list
infile = open("countries.txt", "r")
data = []
for line in infile:
  data.append(line)
infile.close()
print(data)

here = []
for country in data:
    sata_line = country.split("\t")
    he = []
    he.append(sata_line[0])
    he.append(int("".join(sata_line[1].split(",")))/float("".join(sata_line[2].split(","))))
    here.append(he)

print(here)
# Here we split each value in data
# by tab and we use length of value at index 0
# as the dictionary key and the value of corresponding
# value
names = {}
for country in data:
  data_line = country.split("\t")
  try:
      names[len(data_line[0])].append(data_line[0])
  except KeyError:
      names[len(data_line[0])] = [data_line[0]]

for i in sorted(names.keys(), reverse=True):
    for j in sorted(names[i]):
        print(j)


