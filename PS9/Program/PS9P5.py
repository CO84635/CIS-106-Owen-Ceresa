def ComputeTuition(districtcode, credithours):
    if districtcode == "I":
        costperhour = 250.00
    elif districtcode == "O":
        costperhour = 550.00

    tuitionowed = credithours * costperhour

    return tuitionowed

sumtuition = 0.0
r = input("Do you want to run this program? (y/n)")

while r == "y":
    lastname = str(input("What is your lastname?: "))
    districtcode = str(input("What is your district code? (I or O)"))
    credithours = int(input("How many credit hours?"))
    tuitionowed = ComputeTuition(districtcode, credithours)
    sumtuition = sumtuition + tuitionowed
    print(f"Dear {lastname} your tuition owed was {tuitionowed}")

    r = input("Would you like to run this program again?")

print("The sum of tuition was: ", sumtuition)