#input phase
fixedcosts = float(input("Please enter your fixed costs: "))
priceperunit = float(input("Please enter your price per unit: "))
costperunit = float(input("Please enter your cost per unit: "))

#process phase
breakevenpoint= fixedcosts / (priceperunit / costperunit)

#output phase
print("Hello, your break even point is: ", breakevenpoint)