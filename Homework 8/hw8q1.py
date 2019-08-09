'''
M Touhid Chowdhury
mtc405

function to print monthly calander and return what day the next month would begin
function to check leap year
function to build a year calendar


'''

def monthly_calendar(daysInMonth,startingDay):
    '''this function takes in parameter for number of days in month and
    day of the week that represents when calendar begins and prints that month'''
    
    print("Mo\tTu\tWe\tTh\tFr\tSa\tSu\t")

    for number in range(startingDay-1):
            print ("\t", end = "")

    initial = 1
    while initial <= daysInMonth:
        print (" ", initial,end = "\t" )
        if (initial + startingDay - 1) % 7 == 0:
            print ("\n")
        initial += 1

    nextDay = ((daysInMonth-1+startingDay)%7+1)
    print('\n')
    print("next day of the month would begin", nextDay)
    return nextDay

nextDay = monthly_calendar(31,4)
print('\n')

#input 
def check_if_leap_year(year):
    
    leap = False
    if year % 4 == 0 and year % 100 != 0:
        leap = True
    if year % 100 ==0 and year % 400 == 0:
        leap = True
    return leap
userYear= int(input("Please enter a year to check if its leap year or not"))
leap = check_if_leap_year(userYear)
print(leap)

def yearly_calendar(year,startingDay):
    checking = check_if_leap_year(year)
    if checking == True:
        print("\t\t\tJANUARY", year)
        monthly_calendar(31,startingDay)
        print('\n')
        startingDay= ((startingDay+30)%7+1)
        print("\t\t\tFEBUARY", year)
        monthly_calendar(29,startingDay)
        print('\n')
        startingDay=((startingDay+28)%7+1)
        print("\t\t\tMARCH", year)
        monthly_calendar(31,startingDay)
        print('\n')
        startingDay=((startingDay+30)%7+1)
        print("\t\t\tAPRIL", year)
        monthly_calendar(30,startingDay)
        print('\n')
        startingDay=((startingDay+29)%7+1)
        print("\t\t\tMAY", year)
        monthly_calendar(31,startingDay)
        print('\n')
        startingDay=((startingDay+30)%7+1)
        print("\t\t\tJune", year)
        monthly_calendar(30,startingDay)
        print('\n')
        startingDay=((startingDay+29)%7+1)
        print("\t\t\tJuly", year)
        monthly_calendar(31,startingDay)
        print('\n')
        startingDay=((startingDay+30)%7+1)
        print("\t\t\tAugust", year)
        monthly_calendar(31,startingDay)
        print('\n')
        startingDay=((startingDay+30)%7+1)
        print("\t\t\tSeptember", year)
        monthly_calendar(30,startingDay)
        print('\n')
        startingDay=((startingDay+29)%7+1)
        print("\t\t\tOctober", year)
        monthly_calendar(31,startingDay)
        print('\n')
        startingDay=((startingDay+30)%7+1)
        print("\t\t\tNovember", year)
        monthly_calendar(30,startingDay)
        print('\n')
        startingDay=((startingDay+29)%7+1)
        print("\t\t\tDecember", year)
        monthly_calendar(31,startingDay)
    elif checking == False:
        print("\t\t\tJanuary", year)
        monthly_calendar(31,startingDay)
        print('\n')
        startingDay= ((startingDay+30)%7+1)
        print("\t\t\tFebruary", year)
        monthly_calendar(28,startingDay)
        print('\n')
        startingDay=((startingDay+27)%7+1)
        print("\t\t\tMarch", year)
        monthly_calendar(31,startingDay)
        print('\n')
        startingDay=((startingDay+30)%7+1)
        print("\t\t\tApril", year)
        monthly_calendar(30,startingDay)
        print('\n')
        startingDay=((startingDay+29)%7+1)
        print("\t\t\tMay", year)
        monthly_calendar(31,startingDay)
        print('\n')
        startingDay=((startingDay+30)%7+1)
        print("\t\t\tJune", year)
        monthly_calendar(30,startingDay)
        print('\n')
        startingDay=((startingDay+29)%7+1)
        print("\t\t\tJuly", year)
        monthly_calendar(31,startingDay)
        print('\n')
        startingDay=((startingDay+30)%7+1)
        print("\t\t\tAugust", year)
        monthly_calendar(31,startingDay)
        print('\n')
        startingDay=((startingDay+30)%7+1)
        print("\t\t\tSeptember", year)
        monthly_calendar(30,startingDay)
        print('\n')
        startingDay=((startingDay+29)%7+1)
        print("\t\t\tOctober", year)
        monthly_calendar(31,startingDay)
        print('\n')
        startingDay=((startingDay+30)%7+1)
        print("\t\t\tNovember", year)
        monthly_calendar(30,startingDay)
        print('\n')
        startingDay=((startingDay+29)%7+1)
        print("\t\t\tDecember", year)
        monthly_calendar(31,startingDay)
      
def main():
    userYear = int(input("Please enter a year: "))
    userBegin = int(input("Please enter the day to begin year (e.g: 1 for Monday, 2 for Tuesday): "))
    yearly_calendar(userYear,userBegin)
main()
        
        

