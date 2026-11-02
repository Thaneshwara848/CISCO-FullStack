
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="CISCO"
)
cursor = conn.cursor()
# READ Employee ID and New Salary
empid = int(input("Enter Employee ID: "))
salary = float(input("Enter New Salary: "))

# Update Employee Salary
sql = """
UPDATE Employee
SET salary = %s
WHERE id = %s
"""
cursor.execute(sql, (salary, empid))
conn.commit()

if cursor.rowcount > 0:
    print("Employee Salary Updated Successfully!")
else:
    print("Employee Not Found or Salary Already Same!")

cursor.close()
conn.close()
