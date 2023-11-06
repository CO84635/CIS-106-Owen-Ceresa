def AssessedValue(county, marketvalue):
    if county == "Cook":
        AVP = 0.90
    elif county == "Dupage":
        AVP = 0.80
    elif county == "McHenry":
        AVP = 0.75
    elif county == "Kane":
        AVP = 0.60
    else:
        AVP = 0.70
    assessed_value = marketvalue * AVP

    return assessed_value

totalmarket = 0.0
totalav= 0.0

r = str(input("Would run this program? (Y/N): "))
while r == "Y":
    county = str(input("What is your county that you are in?: "))
    marketvalue = float(input("What is your market value?: "))
    assessed_value = AssessedValue(county, marketvalue)
    totalmarket = totalmarket + marketvalue
    totalav = totalav + assessed_value
    print(f"market value is {marketvalue} and assessed value is {assessed_value}")
    r = str(input("Would run this program again? (Y/N): "))

print(f"total av is {totalav} and total market is {totalmarket}")


