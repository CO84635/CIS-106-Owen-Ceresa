lastname = str(input("Please enter your last name:"))
salary = int(input("Please enter your salary: "))
joblevel = float(input("Please enter your job level: "))

if joblevel >= 10:
    bonusrate = 0.25
elif joblevel >= 5:
    bonusrate = 0.20
else:
    bonusrate = 0.10

bonus = salary * bonusrate

print("Dear,", lastname, ", your bonus was: $", bonus)