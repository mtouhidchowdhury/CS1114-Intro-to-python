'''
CS-UY 1114
Professor Frankl
M Touhid Chowdhury
mtc405   N14108583
hw 10
function that randomly creates a permutation, function that adds the
value of two lists if length is equal, function that gives all prefixes,
function that takes menu and then takes order of 3 people.
'''

import random

def create_permutation(lst):
    length = len(lst)
    lim = len(lst)-1
    
    indexes = []
    while len(indexes) < length:
        randomNum = random.randint(0,lim)
        if randomNum in indexes:
            indexes = indexes
        else:
            indexes.append(randomNum)
    for number in indexes:
        lastNum = lst.pop(number)
        lst.append(lastNum)
    return lst

def main_q1():
    print("Q1")
    print("Sample execution using [1,2,3,4,5,6,7]")
    lst = create_permutation([1,2,3,4,5,6,7])
    print(lst)
main_q1()



def add_list(lst1,lst2):
    length = len(lst1)
    newList = []
    for number in range (0,length):
        newList.append(lst1[number]+lst2[number])
    return newList

def main_q2():
    print("Q2")
    lst1 =[]
    lst2 = []
    userInput = 0
    userInput1= 0
    while userInput != 'done':
        userInput = input("Enter one number per line for first lst and 'done' when finished: ")
        if userInput == 'done':
            lst1= lst1
        else:
            lst1.append(int(userInput))
    while userInput1 != 'done':
        userInput1 = input("Enter one number per line for second lst and 'done' when finished: ")
        if userInput1 == 'done':
            lst2= lst2
        else:
            lst2.append(int(userInput1))
    if len(lst1) == len(lst2):
        newList = add_list(lst1,lst2)
        for number in newList:
            print(number)
    else:
        print(" LISTS ARE NOT EQUAL LENGTH!")

main_q2()


def create_prefix_lists(lst):
    copyList = []
    ranges = 0 
    length = len(lst)
    for number in range(0, len(lst)+1):
        copyList.append(lst)
    for number in range(0, len(lst)+1):
        if number == 0:
            copyList[number]= []
        else:
            copyList[number] = copyList[number][0:ranges]
        ranges +=1
        
    return copyList


def main_q3():
    print("Q3")
    print("Sample execution using the list [1,2,3,4]")
    newList = create_prefix_lists([1,2,3,4])
    print(newList)
    
main_q3()



def read_menu():
    user = int(input("How many items in the menu?: "))
    n = 0
    lst = []
    while user > n:
        item = input("Enter item in the form 'name:price': ")
        lst.append(tuple(item.split(':')))
        n+= 1
    return lst
    
def read_order():
    userInput = ''
    newList = []
    while userInput != 'done':
        userInput = input("what do you want to order? Enter 'done' when finished: ")
        if userInput == 'done':
            userInput = userInput
        else:
            newList.append(userInput)
    return newList


def compute_price(menu_list,order_list):
    total = 0
    index = 0 
    for element in order_list:
        for item in menu_list:
            if element in item:
                total += float(item[1])
            index +=1 
    return total

def main_q4():
    print("Q4")
    menu = read_menu()
    customers = 3
    whichCustomer = 1
    while customers != 0:
        print("Hello, you are customer #",whichCustomer,".")
        orders = read_order()
        price = compute_price(menu,orders)
        tax = price * 0.085
        tip =  price * 0.15
        price = price + tip + tax 
        print("Your total is ", round(price,2))
        price = 0
        customers -= 1
        whichCustomer += 1
        
main_q4()
    


