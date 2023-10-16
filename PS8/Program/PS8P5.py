f = open("p5d.txt", "r")

total_tuition = 0
num_students = 0

while True:
    last_name = f.readline().strip()
    if not last_name:
        break
    district_code = f.readline().strip()
    if not district_code:
        break
    credits_taken = int(f.readline().strip())
    if not credits_taken:
        break

    cost_per_credit = 250.00 if district_code == 'I' else 500.00
    tuition_owed = credits_taken * cost_per_credit

    print("Last name:", last_name)
    print("Credits Taken: ", credits_taken)
    print("Tuition Owed: $", tuition_owed)

    total_tuition += tuition_owed
    num_students += 1

print("Total tuition for", num_students, "students: $", total_tuition)