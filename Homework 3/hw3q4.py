#homework 3 question 4

#getting the input of the sides 
a = float(input("Length of first side: "))
b = float(input("Length of second side: "))
c = float(input("Length of third side: "))

if a == b and b == c and a ==c :# if all sides equal equalateral triangle
    print("This is a equilateral triangle")
elif a == b or a == c or b == c:# if two sides equal isosceles triangle
    print("this is a isoseles triangle")
elif (a == b or a == c or b == c) and (a**2 + b**2 == c**2 or a**2 + c**2 == b**2 or c**2 + b**2 == a**2):
    print("this is an isosceles right triangle ")#if two sides equal and pythagorean formula fits its isosceles right triangle
else:#if none of the conditions apply its neither 
    print("neither equalateral nor isosceles right triangle")
    
