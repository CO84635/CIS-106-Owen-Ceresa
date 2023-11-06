
def train_ticket_price(miles):
    if miles >= 30:
        price = 12.00
    elif miles >= 20:
        price = 10.00
    elif miles >= 10:
        price = 8.00
    else:
        price = 5.00
    return price

sumofticket = 0.0
r = str(input("Would you like to run this program? (Y/N)"))

while r == "Y":
    lastname = str(input("What is your last name?"))
    miles = float(input("How many miles away from downtown Chicago are you?"))
    price = train_ticket_price(miles)
    sumofticket = sumofticket + price
    print("Your ticket price was $", price)
    r = str(input("Would you like to run this program again? (Y/N)"))

print("Total amount of all tickets $", sumofticket)