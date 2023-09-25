def computeep(qty, up):
    ep = qty * up

    return ep
#Main
print("Item:      UnitPrice:")
print("A      $10.00")
print("B      $20.00")
print("Which Item?: ")
item = input()
print("What is the quantity: ")
qty = float(input())
if item == ("A"):
    up = 10.00
else:
    up = 20.00
ep = computeep(qty, up)
print("For item:  ", item)
print("The unit price:  $", up)
print("The extended price:  $", ep)