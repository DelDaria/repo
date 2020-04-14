from datetime import date, timedelta


class Employee():
    def __init__(self, name, surname, email, salary):
        self.name = name
        self.surname = surname
        self.email = email
        self.salary = salary

    def work(self):
        return '{} comes to the office!\n'.format(self.name)

    def check_salary(self, days):
        return '{} earns {} for {} days.\n'.format(self.name, self.salary*days, days)

    def month_salary(self):
        now = date.today()
        month_start = date(now.year, now.month, 1)
        weekend = [5, 6]

        diff = (now - month_start).days + 1
        # print(now, month_start, diff)

        day_count = 0

        for day in range(diff):
            # print((month_start + timedelta(day)).weekday())
            if (month_start + timedelta(day)).weekday() not in weekend:
                day_count += 1

        #return day_count
        d = day_count
        return '{}`s month salary is {}.\n'.format(self.name, self.salary*d)

    def __str__(self):
        return '{}: {} {}\n'.format(self.__class__.__name__ , self.name, self.surname)

    def comparison(self, other):
        if self.salary > other.salary:
            return '{} > {}'.format(self.name, other.name)
        elif self.salary < other.salary:
            return '{} < {}'.format(self.name, other.name)
        elif self.salary == other.salary:
            return '{} = {}'.format(self.name, other.name)



    def comparison_tech(self, other):

        if len(self.tech) > len(other.tech):
            return '{} > {}'.format(self.name, other.name)
        elif len(self.tech) < len(other.tech):
            return '{} < {}'.format(self.name, other.name)
        elif len(self.tech) == len(other.tech):
            return '{} = {}'.format(self.name, other.name)



class Recruiter(Employee):
    def __init__(self, name, surname, email, salary, hired_this_month):
        Employee.__init__(self, name, surname, email, salary)
        self.hired = hired_this_month

    def work(self):
        emp_work = super().work()[:-2]
        return emp_work+' for hiring!'



class Programmer(Employee):
    def __init__(self, name, surname, email, salary, closed_this_month):
        Employee.__init__(self, name, surname, email, salary)
        self.closed = closed_this_month
        self.tech = []

    def add_tech(self, skill):
        self.tech.append(skill)

    def tech_stack(self):
        return '{}: {}'.format(self.name, self.tech)

    def work(self):
        emp_work = super().work()[:-1]
        return emp_work + ' for coding!'

    def alpha_programmer(self, other):
        for i in self.tech:
            if i not in other.tech:
                other.tech.append(i)
        return 'Alpha-programmer`s tech stack: {}.'.format(other.tech)





worker = Employee('John', 'Johnson', 'jjj@gmail.com', 100)
print(worker)
print(worker.work())
print(worker.check_salary(2))

worker1 = Recruiter('Stan', 'Stanson', 'ss@gmail.com', 200, 3)
print(worker1)
print(worker1.work())
print('{} hired {} workers.\n'. format(worker1.name, worker1.hired))

print(worker.comparison(worker1))

print()

worker2 = Programmer('Nick', 'Nickson', 'nn@gmail.com', 300, 2)
print(worker2)

worker2.add_tech('1.1')
worker2.add_tech('1.2')

worker3 = Programmer('Jack', 'Jackson', 'jjj@gmail.com', 350, 33)
print(worker3)
worker3.add_tech('1.1')
worker3.add_tech('1.3')
worker3.add_tech('1.4')

print(worker2.tech_stack())
print(worker3.tech_stack())

print(worker2.comparison_tech(worker3))

print(worker2.alpha_programmer(worker3))

print(worker1.month_salary())



