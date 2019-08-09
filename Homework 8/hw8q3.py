

'''
M Touhid Chowdhury
mtc405
 
drawTriangle prints a Triangle given number of lines, the amount of shift , and the character to use
drawTree prints a tree given number of Triangles and the character
main() interacts with the user 
'''

def drawTriangle(integer, shift, character):

    number_of_char = 1
    number_of_spaces = integer + shift - 1
    for i in range(1, integer+1):
        line = ' '*number_of_spaces + character*number_of_char
        print(line)
        number_of_char = number_of_char+2
        number_of_spaces = number_of_spaces-1

def drawTree(numberOfTriangles,character):
    start = 1
    shift= numberOfTriangles -1
    for i in range(2,numberOfTriangles+2):
        drawTriangle(i, shift,character)
        shift-=1
        start+= 1
        numberOfTriangles+=1


def main():
    userCharacter = input("enter character to build with: ")
    userNumberTriangle= int(input("number of triangles: "))
    drawTree(userNumberTriangle,userCharacter)
    
    
main()
    

    
    




