print("What is the name of appliance:  ")
name = input()
print("What is the cost of the appliance:  ")
price = int(input())
if price > 1000.00:
    war = price * 0.1
else:
    war = price * 0.05
total = price + war
print("For the appliance:  ", name, ", and initially costed:  $", str(price), ",with a warranty cost of:  $", str(war),", with a total of:  $", str(total))