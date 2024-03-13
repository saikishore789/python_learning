import csv

fields = ['empid', 'empname', 'empaddress']

rows = [['100', 'sai', 'ap'], ['200', 'kishore', 'TS']]

with open('employee.csv', 'w', newline='') as csvfile:
    # creating a csv writer object
    empwriter = csv.writer(csvfile)
    # writing the fields
    empwriter.writerow(fields)
    # writing the data rows
    empwriter.writerows(rows)

