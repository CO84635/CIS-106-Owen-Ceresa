
numtickets = int(input("Please enter your number of tickets: "))

if numtickets >= 25:
    price = 50
elif numtickets >= 10:
    price = 60
elif numtickets >= 5:
    price = 70
else:
    price = 75

total = numtickets * price

print("Your number of tickets was: ", numtickets)
print("Your price per ticket: $", price)
print("Your total cost was:  $", total)
