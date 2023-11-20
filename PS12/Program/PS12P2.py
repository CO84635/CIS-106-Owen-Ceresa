def display_student_data(names, scores):
    print("Student information is: ")
    for i in range(len(names)):
        print(f"Names: {names[i]}, Scores: {scores[i]}")

def display_student_data_reversed(names, scores):
    print("Student information in Reverse Order: ")
    for i in reversed(range(len(names))):
        print(f"Names: {names[i]}, Scores: {scores[i]} ")

last_names = ["Thompson", "Ceresa", "Hunt", "Batt", "Merlet", "Rymza", "Donlea", "Toniolo", "Dorion", "Haefs"]
exam_scores = [70, 72, 95, 100, 20, 55, 80, 82, 98, 77]

display_student_data(last_names, exam_scores)
display_student_data_reversed(last_names, exam_scores)

