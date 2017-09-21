a = int(input())
b = int(input())
c = int(input())
d = int(input())

if(a < b and c < d):
    for x in range(a, b+1):
        for y in range(c, d+1):
            print("("+ str(x), " " + str(y) + ")", end = "", sep=",")
        print()

if(a > b) and (c > d):
    for x in range(a, b-1, -1):
        for y in range(c, d-1, -1):
            print("("+ str(x), " " + str(y) + ")", sep="," ,end="")
        print()

#a = -1, b = 2, c = 3 and d = 7
#a = 2, b = -1, c = 7 and d = 3