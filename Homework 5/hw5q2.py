
#getting user input
n = int(input("Please enter a positive integer: "))
#spaces
pattern1 =' '
#stars 
pattern2 ='*'
#top triangle prints n lines to form the triangle 
for number in range(0,n):
    line1 =  pattern1*(number) + pattern2* ((n - number) * 2-1 )                 
    print(line1)
#bottom triangle prints n lines to form the triangle 
for number in range(0,n):
    line2 = pattern1 * (n- 1 - number) + pattern2*((number*2) + 1)
    print(line2)

