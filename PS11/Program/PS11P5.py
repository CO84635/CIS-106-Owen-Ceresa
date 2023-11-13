total = 0
tax = 0

def CompTotal(qty, up):
    global total, tax
    total = qty * up
    tax = 0.07 * total

    return tax, total

qty = int(input("Enter the quantity of the item: "))
up = float(input("Enter the unit price of the item: "))
tax, total = CompTotal(qty, up)
print(f"Total: {total}")
print(f"Tax: {tax}")


