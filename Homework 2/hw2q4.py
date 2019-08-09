#adding johns and bills worked time together 

#getting John's data
daysJohn = int(input("Please enter the number of days John worked:"))
hoursJohn = int(input("please enter the number of hours John worked"))
minutesJohn = int(input("please enter the number of minutes John worked"))

#getting bills data
daysBill = int(input("Please enter the number of days Bill worked:"))
hoursBill = int(input("please enter the number of hours Bill worked"))
minutesBill = int(input("please enter the number of minutes Bill worked"))

#adding Johns and Bills data
daysTotal = daysJohn + daysBill
hoursTotal = hoursJohn + hoursBill 
minutesTotal = minutesJohn + minutesBill

#running a loop on the hours to convert them to days 
while hoursTotal >= 24:
    daysTotal = daysTotal + 1
    hoursTotal = hoursTotal - 24
#running a loop on minutes to convert them to hours 
while minutesTotal >= 60:
    hoursTotal = hoursTotal + 1
    minutesTotal = minutesTotal - 60


#printing the data 
print("John and Bill worked in total", daysTotal,"days", hoursTotal,"hours and ",\
      minutesTotal,"minutes")
    


