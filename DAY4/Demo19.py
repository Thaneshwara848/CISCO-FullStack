
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="CISCO"
)

cursor = conn.cursor()

# Read All Employee Records
sql = "SELECT * FROM Employee"

cursor.execute(sql)

employees = cursor.fetchall()

if len(employees) == 0:
    print("No Employees Found!")
else:
    for emp in employees:
        print("Employee ID:", emp[0])
        print("Employee Name:", emp[1])
        print("Employee Age:", emp[2])
        print("Employee Salary:", emp[3])
        print("Employee Designation:", emp[4])
        print("---------------------------")

cursor.close()
conn.close()
