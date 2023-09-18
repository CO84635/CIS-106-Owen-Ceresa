#input phase
totalofmeal = float(input("Please enter the total of the meal: "))

#process phase
fifteenpercent = totalofmeal * .15
fifteenpercenttotal= totalofmeal + fifteenpercent
eightteenpercent = totalofmeal * .18
eightteenpercenttotal= totalofmeal + eightteenpercent
twentypercent = totalofmeal * .20
twentypercenttotal= totalofmeal + twentypercent

#Output phase
print("With 15% Tip:")
print("Total: ", totalofmeal)
print("Tip:", fifteenpercent)
print("Total of meal with tip: ", fifteenpercenttotal)

print("With 18% Tip:")
print("Total: ", totalofmeal)
print("Tip:", eightteenpercent)
print("Total of meal with tip: ", eightteenpercenttotal)

print("With 20% tip: ")
print("Total: ", totalofmeal)
print("Tip:", twentypercent)
print("Total of meal with tip: ", twentypercenttotal)