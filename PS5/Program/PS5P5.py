lastname = input("Enter last name: ")
grosspay = input("Enter your gross income: ")
nodep = input("Enter dependents: ")

adjgross = float(grosspay) - 12000.00 * float(nodep)

if adjgross > 50000.00:
    tax = adjgross * 0.20
else:
    tax = adjgross * 0.10

    if tax < 0:
        tax = 100.00

print(lastname)
print("Gross income: $", grosspay)
print("Number of Dependents: ", nodep)
print("Adjusted Gross:   $", adjgross)
print("Income Tax:   $", tax)
