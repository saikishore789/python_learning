import csv
import mysql.connector
from mysql.connector import Error
from mysql.connector import errorcode

try:
    connection = mysql.connector.connect(host='localhost',
                                         database='mysql',
                                         user='admin',
                                         password='saikishore')
    mysql_empsql_insert_query = "INSERT INTO studentdata (name, branch, year, cgpa) VALUES  (%s, %s, %s)"

    rows = []
    with open('employee.csv', 'r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            rows.append(row.values())
    cursor = connection.cursor()
    cursor.executemany(mysql_empsql_insert_query,rows)
    connection.commit()
    print(cursor.rowcount, "record successfully inserted")

    sql_select_query = "select * from empdata"
    cursor = connection.cursor()
    cursor.execute(sql_select_query)
    records = cursor.fetchall()
    print("total no.of rows in employee table is:", cursor.rowcount)

    print("printing each employee record")
    for row in records:
        print("name = ", row[0])
        print("branch = ", row[1])
        print("year = ", row[2])
        print("cgpa = ", row[3])
    cursor.close()
except mysql.connector.Error as error:
    print("failed to insert record {}", format(error))

finally:
    if (connection.is_connected()):
        connection.close()
        print("mysql connection is closed")