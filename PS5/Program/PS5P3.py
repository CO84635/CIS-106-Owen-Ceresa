def computetotal(qty, cst):
    total = qty * cst

    return total
#main
print("How many books: ")
qty = float(input())
print("What is the cost: ")
cst = float(input())
total = computetotal(qty, cst)
if total > 50.00:
    sp = 0.00
else:
    sp = 25.00
odrtotal = total + sp
print("Your order total:  $", odrtotal)
print("Your shipping is:  $", sp)


