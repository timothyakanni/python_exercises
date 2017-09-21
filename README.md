# python_exercises
My python exercises codes

#Number statistics Question 3


count = 0
sum = 0.0
mean = 0.0
Max = 0.0

line = input()
Min = float(input())
while (line != ""):
    line_input = float(line)

    # Here we calculated the sum
    sum = sum + line_input
    count = count + 1

    # Here we calculate the mean
    mean = (sum/count)

    #Here we find the Maximumum value
    if (Max < line_input):
        Max = line_input

    # Here we find the Minimum value

    if (Min > line_input):
        Min = line_input

    line = input()

print("The Sum of " + str(count) + " given numbers is: " + str(sum))
print("The Mean of " + str(count) + " given numbers is: " + str(mean))
print("The Maximun of " + str(count) + " given numbers is: " + str(Max))
print("The Minimum " + str(count) + " given numbers is: " + str(Min))
# Here the input has ended. Now it is time to compute and print results.
