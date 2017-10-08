# Number Picker --- Done

import sys

#Add your pickNumbers function definition below

def pickNumbers(filename):
    init = []
    # here we read the file line by line
    infile = open(filename, "r")
    for line in infile:
        # here we remove new line with strip and split with space
        data_line = line.strip("\n").split(" ")
        for val in data_line:
            #print(val)
            if(val.isdecimal()):
                init.append(int(val))
    infile.close()
    return init

numbers = pickNumbers("numbers.txt")
for i in range(len(numbers)):
  if type(numbers[i]) != int:
    sys.exit()
  if i > 0 and i % 10 == 0:
    print()
  print(" " + str(numbers[i]), end="")
print()