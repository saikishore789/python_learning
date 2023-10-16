#expenses = [10.20, 3, 70, 30]

total = 0 
expenses = []

num_expenses = int(input("enter no of elements in range: "))

for i in range(num_expenses):
    expenses.append(float(input("enter an expense:")))

total = sum(expenses)

"""
sum = 0

for x in expenses:
    sum = sum + x 
"""

print('you spent $', total, sep = '')