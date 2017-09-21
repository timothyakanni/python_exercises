a = float(input())
b = float(input())
c = float(input())

s1 = (-b - (b**2 - 4*a*c)**(0.5))/(2*a)

s2 = (-b + (b**2 - 4*a*c)**(0.5))/(2*a)

# "1", "-0.5" and "-1.5"
if(s1 == s2):
    print("One distinct real solution")

    if(b < 0):
        print("The equation " + str(a) + "x^2 - " + str(abs(b)) + "x " + " " + str(c) + " = 0 "
              + "has one distinct real solution: x = " + str(s1))

    if(c < 0):
        print("The equation " + str(a) + "x^2 + " + str(b) + "x - " + str(abs(c)) + " = 0 "
              + "has one distinct real solution: x = " + str(int(s1)))

    if(b < 0 and c < 0):
        print("The equation " + str(a) + "x^2 - " + str(b) + "x " + "- " + str(c) + " = 0 "
              + "has one distinct real solution: x = " + str(s1))

elif(s1 != s2 and (isinstance(s1, complex) == False or isinstance(s2, complex) == False)):
    print("Two different real solution")

    if (a == 1 and b < 0 and c < 0):
        print("The equation x^2 - " + str(abs(b)) + "x " + " - " + str(abs(c)) + " = 0 "
              + "has two distinct real solution: x = " + str(int(s1)) + " and x = " + str(s2))
    if(b < 0 and a != 1):
        print("The equation " + str(a) + "x^2 - " + str(abs(b)) + "x " + "+ " + str(c) + " = 0 "
              + "has two distinct real solutions: x = " + str(round(s1,3)) + " and x = " + str(round(s2,3)))

elif(isinstance(s1, complex) or isinstance(s2, complex)):
    print("The equation " + str(int(a)) + "x^2 + " + str(int(c)) +
          " = 0 has no real solution!")

#The equation x^2 - 0.5x - 1.5 = 0 has two distinct real solutions: x = -1 and x = 1.5
#-The equation 1.0x^2 - 0.5x + -1.5 = 0 has two distinct real solutions: x = -1.0 and x = 1.5

#+The equation 1.5x^2 - 2.5x + 0.5 = 0 has two distinct real solutions: x = 0.232 and x = 1.434
print(s1)
print(s2)

#"-1.25", "2.5" and "-1.25"
#"The equation -1.25x^2 + 2.5x - 1.25 = 0 has one distinct real solution: x = 1".

#The equation x^2 - 0.5x - 1.5 = 0 has two distinct real solutions: x = -1 and x = 1.5"
#"The equation 2x^2 + 2 = 0 has no real solution!"