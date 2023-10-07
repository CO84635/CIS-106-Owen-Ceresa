#input phase
principle = int(input("Please enter your principle amount for CD:  $"))
maturity = float(input("Please enter your maturity of CD:  "))

#process
if principle > 100000.00 and maturity == 5:
    intrate = 0.06
elif principle > 50000.00 and maturity == 10:
    intrate = 0.05
elif principle > 50000.00 and maturity == 5:
    intrate = 0.04
else:
    intrate = 0.02

#output
firstyear = principle * intrate
print("Your principle was:  $", principle)
print("your interest rate was: ", intrate)
print("Your interest amount for first year: $", firstyear)



