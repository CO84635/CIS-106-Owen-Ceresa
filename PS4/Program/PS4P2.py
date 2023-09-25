#input phase
pricepershare = float(input("Enter the price per share: "))
currentstock = float(input("Enter the current stock: "))
quantityofstock = float(input("enter the quantityofstock: "))

#process phase
Value = (currentstock - pricepershare) * quantityofstock

#output phase
print("Here is the value of your stock (If negative that means that you are losing money: ", Value)
