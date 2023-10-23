def CompMPG(miles, gal):
    mpg = miles / gal

    return mpg

entries = 0
r = input("Do you want to compute Miles Per Gallon Calculator? (y/n)")

while r == "y":
    dest = str(input("What is the destination: "))
    miles = float(input("What is the miles driven: "))
    gal = float(input("What is the gallons used: "))
    mpg = CompMPG(miles, gal)
    entries = entries + 1
    print(f"For {dest} there was {miles} miles and a {mpg} mpg")
    r = input("Do you want to run the Miles Per Gallon Calculator? (y/n) ")

print(f"Total amount of entries made {entries}.")
