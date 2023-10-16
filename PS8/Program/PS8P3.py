
f = open("p3d.txt", "r")


totbon = 0.0


while True:
    last_name = f.readline().strip()
    salary_str = f.readline().strip()

    if not last_name or not salary_str:
        break

    salary = float(salary_str.replace(',', ''))


    if salary >= 100000.00:
        br = 0.20
    elif salary >= 50000.00:
        br = 0.15
    else:
        br = 0.0

    bonus = salary * br
    totbon += bonus


    print("Lastname:", last_name)
    print("Salary: $", salary)
    print("Bonus: $", bonus)
    print("Total bonuses:", totbon)


f.close()

