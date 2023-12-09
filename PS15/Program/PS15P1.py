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
class Manager(Employee):
    def long_term_bonus(self):
        long_term_bonus = 0.4 * self.pay
        return long_term_bonus

mgr_1 = Manager('Brandon', 'Thompson', 0.10, 75000)
mgr_2 = Manager('First', 'Lastname', 0.15, 50000)

print(mgr_1.fullname(), mgr_1.bonus(), mgr_1.long_term_bonus())
print(mgr_2.fullname(), mgr_2.bonus(), mgr_2.long_term_bonus())