# Primes Part2 ----Done

import itertools
import sys
#Implement your primes generator below
# Note lowerBound parameter is a default parameter
# with value 2 when the parameter is not given in
# the functions. check types of function paramter
# https://www.tutorialspoint.com/python/python_functions.htm

def primes(NprimeNumber, lowerBound = 2):
    count = 0

    for pnum in itertools.count(lowerBound):
            for i in range(2, pnum):
                if (pnum % i) == 0:
                    break
            else:
                yield pnum
                count = count + 1
                if (count == int(NprimeNumber)):
                    break

#Implement your primes generator above
if len(sys.argv) == 2:
  for prime in primes(int(sys.argv[1])):
    print(" " + str(prime), end="")
elif len(sys.argv) == 3:
  for prime in primes(int(sys.argv[1]), int(sys.argv[2])):
    print(" " + str(prime), end="")
print()