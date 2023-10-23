def CompPayRate(jobcode, hrs):
    if jobcode == "L":
        payrate = 25.00
    elif jobcode == "A":
        payrate = 30.00
    elif jobcode == "J":
        payrate = 50.00

    if hrs >= 40.00:
        grosspay = (payrate * (40 + ((hrs -40) * 1.5)))
    else:
        grosspay = (payrate * hrs)

    return grosspay

totalgrosspay = 0.0
r = input("Do you want to run this program? (y/n)")

while r == "y":
    lastname = str(input("What is your last name?"))
    jobcode = str(input("Please enter your Job Code: (L,A,J)"))
    hrs = float(input("How many hours: "))
    grosspay = CompPayRate(jobcode, hrs)
    totalgrosspay = totalgrosspay + grosspay
    print(f" Dear {lastname} your grosspay was $ {grosspay}")
    r = input("Do you want to run this program again? (y/n)")

print("Total grosspay: $", totalgrosspay)

