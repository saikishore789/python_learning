import csv

mydict = [{'branch': 'CSE', 'cgpa': '9.0',
           'name': 'Nikhil', 'year': '2'},
          {'branch': 'CSE', 'cgpa': '9.1',
           'name': 'Sanchit', 'year': '2'},
          {'branch': 'IT', 'cgpa': '9.3',
           'name': 'Aditya', 'year': '2'},
          {'branch': 'EEE', 'cgpa': '9.5',
           'name': 'Sagar', 'year': '1'},
          {'branch': 'MCA', 'cgpa': '7.8',
           'name': 'Prateek', 'year': '3'}]

fields = ['name', 'branch', 'year', 'cgpa']

with open('employee.csv', 'w', newline='') as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=fields)

    writer.writeheader()
    writer.writerows(mydict)
