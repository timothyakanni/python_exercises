# Soduku --- Done

ch_list = []
for ch in "8239574166748215939516542874862" \
          "15739539768124217349865762583941345192678198476352":
    ch_list.append(ch)

for k in range(3):  # created first structure and duplicate 3 times
    for i in range(37): #i first line of # only
         print("#", end="")
    print("")
    for m in range(5): # duplicate second line in code below 5 times
        for j in range(37): # created second line and use range of 5 above to dupliace 5 times
            if (j%12 == 0):
                print("#", end="")
            elif(j%4 == 0 and m%2 == 0):
                print("|", end="")
            elif(j%4 == 0 and m%2 != 0):
                print("+", end="")
            elif (m % 2 != 0):
                print("-", end="")
            elif (j%2 == 0):
                    # put the first character in the ch_list and remove the
                    # character from the list
                    print(ch_list[0], end="")
                    del ch_list[0]
            else:
                print(" ", end="")
        print("")

for i in range(37): # last line of # only
    print("#", end="")

print()