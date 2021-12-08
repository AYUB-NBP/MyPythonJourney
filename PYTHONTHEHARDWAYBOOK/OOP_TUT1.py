class Employee(object):
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay

    def fullName(self):
        print(f'{self.first} {self.last}')


emp_1 = Employee('Ayoub', 'Mellouk', '10000000000$')
emp_2 = Employee('Omar', 'Hajjine', '1000000000000000000000$')
emp_1.fullName()
print(emp_1.pay)
emp_2.fullName()
print(emp_2.pay)
