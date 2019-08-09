import math  #importing a module

#getting users input
a = float(input("Please enter a value for a: "))
b = float(input("Please enter a value for b: "))
c = float(input("Please enter a value for c: "))

#calculating discrimant to see how many solutions
discrimant = b**2 - (4 * a * c )

if a == 0 and b == 0 and c == 0:
    print("this equation has infinite number of solutions.")#infinite
elif a == 0 and b == 0 and c != 0:
    print("this equation has no solutions.")#no solution
elif discrimant < 0:
    print("There is no real solutions")#if discrimant negative no solution

elif a!=0 and discrimant == 0:
    solution = (-b + math.sqrt(discrimant)) / (2 * a)
    print ("This equation has one solutions: ", solution)#if discrimant equals 0 one solution
elif a != 0 and discrimant > 0:
    solution1 = (-b + math.sqrt(discrimant)) / (2 * a)#solution1 1 
    solution2 = (-b - math.sqrt(discrimant)) / (2 * a)#solution 2 
    print("This equation has two solutions: x = ", solution1, "and x = ", solution2)#discrimant greater than 0
elif a ==0 and b!= 0 and c != 0:#linear
    solut = -c/b
    print(' the equation has single solution x =', solut)
elif a == 0 and b!=0 and c ==0:
    print("this equation has single real solution x =0")
