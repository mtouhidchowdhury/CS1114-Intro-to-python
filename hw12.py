'''

M. Touhid Chowdhury
mtc405
N14108580
Professor Frankl
HW 12
Note: used the windows file
had extra lines so removed that using if statement 

'''


def function(file,user):
    file = open(file, 'r')
    empty = []
    header = file.readline()
    string = ""
    for line in file:
        line = line.strip()
        lst = line.split(',,')
        if '' not in lst:
            Id = lst[0]
            stop = lst[1]
            train_line = Id[0]
            if train_line == str(user):
                if stop not in empty:
                    empty.append(stop)
    if empty == []:
        print("This train line does not exist")
    else:
        print(user, "line:", end = ' ')
        for stop in empty:
            string += stop+ ", "
    print(string[:-2])
    print("\n")
        

def main():
    keepGoing = True
    while keepGoing:
        user = input("Enter a train line or 'done' to stop: ").upper()
        if user.upper() != 'DONE':
            function('train stop data-Windows.csv', user)
        else:
            keepGoing = False
main()

            
