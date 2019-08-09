#getting user integer
integer = int(input("Please enter a positive integer: "))
#assign respective roman numeral to its value
I = 1
V = 5
X = 10
L = 50
C = 100
D = 500
M = 1000

roman =""
while integer >= M:
    integer = integer - 1000
    roman+= "M"
while integer >= D:
    integer = integer - 500
    roman+= "D"
while integer >= C:
    integer = integer - 100
    roman+= "C"
while integer >= L:
    integer = integer - 50
    roman+= "L"
while integer >= X:
    integer = integer - 10
    roman+= "X"
while integer >= V:
    integer = integer - 5
    roman+= "V"
while integer >= I:
    integer = integer - 1
    roman+= "I"
print(roman)
