import csv

outlist=[]
with open('employee.csv', 'r', newline='') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        print(row)
        print(row['name'], row['branch'])
        outlist.append(row.values())
    
    print(outlist)