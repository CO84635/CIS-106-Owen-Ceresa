print("Would you like to do this program? (Yes or No): ")
response = str(input())
sumgrosspay = 0.0
numofemployees = 0
while response == "Yes":
    print("Enter your last name")
    lastname = str(input())
    print("Enter hours worked: ")
    hours = int(input())
    print("Enter your pay rate: $")
    rate = float(input())
    if hours >= 40:
        grosspay = 40 * rate + (hours - 40) * 1.5 * rate
    else:
        grosspay = hours * rate
    print("Dear, " + lastname ,", your gross pay is $" +str(grosspay))
    sumgrosspay = sumgrosspay + grosspay
    numofemployees= numofemployees + 1
    print("Would you like to run this program again?: ")
    response = str(input())
avggrosspay = sumgrosspay / numofemployees
print("Sum of all gross pay is: $" + str(sumgrosspay))
print("Number of employees is: " + str(numofemployees))
print("Average gross pay is: " + str(avggrosspay))




