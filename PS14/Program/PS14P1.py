

class Employee:

    def __init__(self, first, last, rate, pay):
        self.first = first
        self.last = last
        self.rate = rate
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def bonus(self):
        bonus = (self.pay * self.rate)
        return bonus


emp_1 = Employee('Corey', 'Schafer', 0.05, 50000)
emp_2 = Employee('Test', 'User', 0.1, 60000)

print(Employee.fullname(emp_1), Employee.bonus(emp_1))
