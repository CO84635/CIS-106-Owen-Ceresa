

class Student:

    def __init__(self, first, last, d_code, enrolled_credits):
        self.first = first
        self.last = last
        self.d_code = d_code
        self.enrolled_credits = enrolled_credits

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    def tuition_owed(self):
        if self.d_code == 'I':
            credit_hour = 250.00
        else:
            credit_hour = 500.00
        return credit_hour

        tuition_owed = (credit_hour * enrolled_credits)
        return tuition_owed

stud_1 = Student('Brandon', 'Thompson', 'I', '15')
stud_2 = Student('Owen', 'Ceresa', 'O', '10')

print(Student.fullname(stud_1), Student.tuition_owed(stud_1))
print(Student.fullname(stud_2), Student.tuition_owed(stud_2))