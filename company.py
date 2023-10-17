from employee import Employee

class Company:
    def __init__(self):
        self.employees = []

    def add_employee(self, new_employee):
        self.employees.append(new_employee)
    
    def display_employees(self):
        print('current employees:')
        for i in self.employees:
            print(i.fname, i.lname)
        print('--------')

    def salary_display(self):
        print('current employee monthly salary')
        for i in self.employees:
            print('salary of', i.fname, i.lname)
            print('amount:', i.calculate_paychecker())
            print('--------')

def main():
    my_company = Company()

    employee1 = Employee('sai', 'kishore', 1000000)
    my_company.add_employee(employee1)
    employee2 = Employee('viswa', 'Reddy', 500000)
    my_company.add_employee(employee2)

    my_company.display_employees()
    my_company.salary_display()

main()

