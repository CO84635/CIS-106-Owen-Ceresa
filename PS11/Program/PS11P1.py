def CompDiscount(qty, price, DiscRate):
    tprice = price * qty
    discount =  tprice * DiscRate
    disc_price = tprice - discount
    return discount, disc_price

qty = int(input("What is the quantity of product?: "))
price = int(input("What is the price of the product?: "))
DiscRate = float(input("What is the discount rate of the product?: "))
discount, disc_price = CompDiscount(qty, price, DiscRate)
print(f"The discount amount ${discount}, with a discounted total price of ${disc_price}")
print(f"Quantity is {qty} & price is {price} & discount rate of {DiscRate}")