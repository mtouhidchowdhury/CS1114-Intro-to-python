'''
CS-UY 1114
Professor Frankl
M Touhid Chowdhury
mtc405  N14108583
hw 9
function to give the maximum absolute value, function to find all indexes of given value,
function that reverses string, another function that reverses in place, function that encodes a string,
function that decodes the string
'''

def max_abs_val(lst):
    index = 0
    lengthOfLst= len(lst)
    while index < lengthOfLst:
        if lst[index] < 0:
            newNumber = lst[index] * -1
            lst.pop(index)
            lst.insert(index,newNumber)
        index += 1
    firstNumber = lst[0]
    for numbers in lst:
        if numbers > firstNumber:
            firstNumber = numbers
    return firstNumber 

def main_q1():
    print("Q1")
    print(" Sample execution using [-19, -3, 20, -1, 0, -25] : ")
    lst = [-19, -3, 20, -1, 0, -25]
    maximum = max_abs_val(lst)
    print(maximum)
main_q1()

def find_all(lst, val):
    index = 0
    newList = []
    for number in lst:
        if number == val:
            newList.append(index)
        index +=1
    return newList

def main_q2():
    print("Q2")
    print("Sample execution using [‘a’, ‘b’, 10, ‘bb’, ‘a’] and 'a'")
    lst = ['a', 'b', 10, 'bb', 'a']
    value = 'a'
    newList = find_all(lst, value)
    print(newList)
main_q2()


def reverse1 (lst):
    newList =[]
    endingIndex = len(lst)-1 
    while endingIndex >= 0:
        newList.append(lst[endingIndex])
        endingIndex -= 1 
    return newList 

def reverse2 (lst):
    indexs= len(lst)-1
    index= 0 
    while indexs > index:
        lst.append(lst[indexs-1])
        lst.pop(indexs-1)
        indexs -= 1
    return lst 

def main_q3():
    print("Q3")
    lst1 = [1, 2, 3, 4, 5, 6]
    rev_lst1 = reverse1(lst1)
    print("After reverse1, lst1 is ", lst1, " and the returned list is ", rev_lst1)
    lst2 = [1, 2, 3, 4, 5, 6]
    reverse2(lst2)
    print("After reverse2, lst2 is ", lst2)

main_q3()


def encoder(string):
    encodedList = []
    counter = 1
    length = len(string)
    for index in range(0,length):
        if index < (length-1): 
            if string[index] == string[index+1]: 
                counter+= 1
            elif string[index] != string[index+1]:
                encodedList.append([string[index],counter]) 
                counter = 1 
        elif index == (length-1): 
            if string[index] == string[index-1]: 
                counter += 1
                encodedList.append([string[index],counter-1]) 
            else:
                encodedList.append([string[index],counter])
                counter = 1
    return encodedList

 
def decode(lst):
    string = ""
    for character, numberOfCharacters in lst:
        string += character * numberOfCharacters
    return string
 
def main_q4():
    print("Q4")
    print(" String is 'aadccccaa' decoding will give: ")
    string= 'aadccccaa'
    encoded = encoder(string)
    print(encoded)
    print("Encoded to string is: ")
    backToString = decode(encoded)
    print(backToString)

main_q4()















    
    
