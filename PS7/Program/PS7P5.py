print("Do you want to calculate total order with discount? (Yes or No) : ")
response = str(input())
sumofdiscamt = 0.0
numoforder = 0
while response == "Yes":
    print("What is the quantity: ")
    qty = int(input())
    print("Please enter the price: $")
    price = float(input())
    extprice = qty * price
    if extprice > 10000.00:
        discamt = extprice * 0.25
    else:
        discamt = extprice * 0.10
    totalorder= extprice - discamt
    sumofdiscamt = sumofdiscamt + discamt
    numoforder = numoforder + 1
    print("Extended price is $: " + str(extprice))
    print("Discount earned $: " + str(discamt))
    print("Total order amount: $" + str(totalorder))
    print("Would you like to order again (Yes or No): ")
    response = input()
print("Total Discounts given $: " + str(sumofdiscamt))
print("Number of orders entered: " + str(numoforder))
avgdiscamt = sumofdiscamt / numoforder
print("Your average discount given $: " + str(avgdiscamt))


