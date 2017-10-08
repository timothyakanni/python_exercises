# Country Population Filter ---Done
# The objective of this task is to filter specified filename where
# each line contain country names with their population and area
# separated by tab. The function called popDensityFilter is used to
# process the filename and calculate country density.
from sys import argv

#Implement your popDensityFilter generator below
def popDensityFilter(filename, lowDensity = 0.0, highDensity= float("Infinity")):

    # Here the line in given filename is read line by line and append to data list
    data = []
    infile = open(filename, "r")
    for line in infile:
        data.append(line)
    infile.close()

    # Here each information in data list is splitted by tab delimiter
    # and we take value by there index, index 0 for country name
    # index 1 for population and index 2 for area and we get density
    # by divide population by area and append name and density value to
    # result list
    for country in data:
        splitted_line = country.split("\t")
        result = []
        result.append(splitted_line[0])
        density = int("".join(splitted_line[1].split(","))) / float("".join(splitted_line[2].split(",")))
        result.append(density)
        if(density >= lowDensity and density <= highDensity):
            yield result

#Implement your popDensityFilter generator above
if len(argv) == 2:
  for country, density in popDensityFilter(argv[1]):
    print(country, round(density, 2))
elif len(argv) == 3:
  low = float(argv[2])
  for country, density in popDensityFilter(argv[1], low):
    print(country, round(density, 2))
elif len(argv) == 4:
  low = float(argv[2])
  high = float(argv[3])
  for country, density in popDensityFilter(argv[1], low, high):
    print(country, round(density, 2))