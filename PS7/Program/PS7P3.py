print("Would you like to run this program? ")
response = input()
numofstudents = 0
while response == "Yes":
    print("What is your lastname")
    lastname = input()
    print("What was your first exam score: ")
    exam1 = float(input())
    print("What was your second exam score: ")
    exam2 = float(input())
    average = float(exam1 + exam2)/2
    print("Dear, " + lastname,", your average exam score was: " + str(average))
    numofstudents = numofstudents + 1
    print("Would you like to runm this program again?")
    response = input()
print("Number of students who entered data: " + str(numofstudents))