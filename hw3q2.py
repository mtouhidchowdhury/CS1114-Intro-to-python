#hw 3 question 2

#getting user input
firstItem = float(input(" Enter price of first item: "))
secondItem = float(input ("Enter price of second item: "))
total = firstItem + secondItem#total before discount
#comparing prices to give 50% discount
if firstItem > secondItem:
    secondItem1 = secondItem * 0.5
    firstItem1 = firstItem
elif secondItem > firstItem:
    firstItem1 = firstItem * 0.5
    secondItem1 = secondItem
elif secondItem == firstItem:
    secondItem1 = secondItem * 0.5
    firstItem1 = firstItem
#first discount total
totalWithFirstDiscount = firstItem1 + secondItem1
#asking user if they are members
membership = input("Does customer have a club card? Enter Y/N: ")
#if member apply 10% discount
if membership == 'Y' or 'y':
    secondDiscount = totalWithFirstDiscount * 0.10
    totalWithSecondDiscount = totalWithFirstDiscount - secondDiscount
elif  membership == 'N' or 'n':
    totalWithSecondDiscount = totalWithFirstDiscount
#asking for tax rate
taxrate = float(input("Enter tax rate, e.g. 5.5 for 5.5% tax: "))
#calculating tax
tax = totalWithSecondDiscount * (taxrate/100)
#calculating total with both discounts and tax
totalPrice = totalWithSecondDiscount + tax
#printing results 
print("Base price = ",round(total,2))
print("Price after discounts = ",round(totalWithSecondDiscount,2))
print("Total price: ", round(totalPrice,2))

    
