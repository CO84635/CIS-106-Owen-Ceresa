#input phase
firstname = input("Please enter your first name: ")
Steps = float(input("Please enter the amount of steps today: "))

#process phase
Caloriesburned = Steps * .25

#output phase
print("Dear,",firstname, "You have burned", Caloriesburned,"Calories.")