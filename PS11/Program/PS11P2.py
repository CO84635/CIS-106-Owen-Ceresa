def computeexam(exam1, exam2, exam3,):
    AvgExam = (exam1 + exam2 + exam3) / 3
    TotalExam = (exam1 + exam2 + exam3)

    return AvgExam, TotalExam

lastname = str(input("What is your lastname?: "))
exam1 = float(input("What is your first exam score?: "))
exam2 = float(input("What is your second exam score?: "))
exam3 = float(input("What is your third exam score?: "))
AvgExam, TotalExam = computeexam(exam1,exam2,exam3)
print(f"Dear {lastname}, your total was {TotalExam} and an average exam score of {AvgExam}")

