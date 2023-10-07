#input phase
qty =int(input("Please enter the quantity of order: "))

#process phase
if qty >10000:
    price = 10.00
elif qty > 5000:
    price = 20.00
elif qty < 5000:
    price = 30.00

#output phase
extprice = qty * price
tax = extprice * 0.07
total = extprice + tax

print("Your extended price is:  $", extprice)
print("Your tax was:  &", tax)
print("Your total was:  $", total)
