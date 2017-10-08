# Word Length Filter --- Done

import sys
#Implement your wordLenFilter generator below

def wordLenFilter(filename, wordLen):
    # here we read the file line by line
    infile = open(filename, "r")
    for line in infile:
        data_line = line.strip("\n").split(" ")
        for val in data_line:
            # print(val)
            if (len(val) == wordLen):
                yield val
    infile.close()
#Implement your wordLenFilter generator above
for i, word in enumerate(wordLenFilter("words.txt", int(7))):
  if i > 0 and i % 10 == 0:
    print()
  print(" " + word, end="")
print()