mydata_txt = "mydata.txt"
lname = []
exam_scores = []

def loadarrays(file_path, lname, exam_scores):
    with open(file_path, "r") as file:
        for line in file:
            data = line.strip().split(',')
            lname.append(data[0])
            exam_scores.append(int(data[1]))

    return lname, exam_scores

def display_student_data(lname, exam_scores):
    print("Student Data:")
    for i in range(len(lname)):
        print(f"Name: {lname[i]}, Exam Score: {exam_scores[i]}")

def display_High_and_Low(lname, exam_scores):
    high_score = 0
    low_score = 100  # Assuming scores are between 0 and 100
    high_score_index = 0
    low_score_index = 0

    for i in range(len(exam_scores)):
        if exam_scores[i] > high_score:
            high_score = exam_scores[i]
            high_score_index = i
        if exam_scores[i] < low_score:
            low_score = exam_scores[i]
            low_score_index = i

    print(f"Highest Score: {lname[high_score_index]} - {high_score}")
    print(f"Lowest Score: {lname[low_score_index]} - {low_score}")

loadarrays(mydata_txt, lname, exam_scores)
display_student_data(lname, exam_scores)
display_High_and_Low(lname, exam_scores)
