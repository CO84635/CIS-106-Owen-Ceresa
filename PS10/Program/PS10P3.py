
def otd_price(msrp, make, model):
    if make == "Honda" and model == "Accord":
        disc_perc = 0.10
    elif make == "Toyota" and model == "Rav4":
        disc_perc = 0.15
    else:
        disc_perc = 0.05
    pricenotax = (msrp - (msrp * disc_perc))
    price = pricenotax + (pricenotax * 0.07)

    return price
totalmsrp = 0.0
totalprice = 0.0
r = str(input("Would you like to run this program? (Y/N): "))
while r == "Y":
    make = str(input("What is the make?: "))
    model = str(input("What is the model?: "))
    msrp = float(input("What is the MSRP?: "))
    price = otd_price(msrp, make, model)
    print(f"Price is $ {price}" )
    totalmsrp = totalmsrp + msrp
    totalprice = totalprice + price
    r = str(input("Would you like to run this program again? (Y/N)"))

print(f"total msrp is {totalmsrp} and total price is {totalprice}")