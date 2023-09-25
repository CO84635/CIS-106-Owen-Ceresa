def computeep(qty, up):
    ep = qty * up

    return ep
#Main
print("Please enter the quantity: ")
qty= float(input())
if qty >= 1000.00:
    up = 3.0
else:
    up = 5.0
ep = computeep(qty, up)
tax = ep * 0.07
total = ep + tax
print("Your quantity is:" + str(qty))
print("Your unit price:  $" + str(up))
print("Your extended price:  $" + str(ep))
print("Your tax is:  $" + str(tax))
print("Your total is:  $" + str(total))
