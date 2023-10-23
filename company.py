from employee import Employee, SalaryEmployee, HourlyEmployee, CommissionEmployee

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
            print(f'amount:, ${i.calculate_paychecker():,.2f}')
            print('--------')

def main():
    my_company = Company()

    employee1 = SalaryEmployee('sai', 'kishore', 1000000)
    my_company.add_employee(employee1)
    employee2 = HourlyEmployee('viswa', 'Reddy', 40, 50)
    my_company.add_employee(employee2)
    employee3 = CommissionEmployee('Sai', 'Reddy', 400000, 5, 60)
    my_company.add_employee(employee3)

    my_company.display_employees()
    my_company.salary_display()

main()

