# World Length Group --- Done
import sys

wordLength = {}
infile = open("words2.txt", "r")
for line in infile:
    data_line = line.strip(" ").split("\n")
    for val in data_line:
        try:
            wordLength[len(val)].append(val)
        except KeyError:
            wordLength[len(val)] = [val]
infile.close()
print(wordLength)

for i in sorted(wordLength.keys()):
    print(" ".join(sorted(wordLength[i])))

