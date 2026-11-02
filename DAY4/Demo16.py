import mysql.connector
conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="CISCO"
    )

cursor = conn.cursor();

                    #CHECK / READ

empid = int(input("Enter Employee ID: "))
name = input("Enter Employee Name: ")
age = int(input("Enter Employee Age: "))
salary = float(input("Enter Employee Salary: "))
desig = input("Enter Employee Designation: ")

# Insert Employee
sql = """
INSERT INTO Employee (id, name, age, salary, desig)
VALUES (%s, %s, %s, %s, %s)
"""
cursor.execute(sql, (empid, name, age, salary, desig))
conn.commit()
print("Employee Added Successfully!")
cursor.close()
conn.close()

# Store in Tuple    
# employee = (empid, name, age, salary, desig)   
# INSTED oF THIS i want to STORE in MYSQL DB 



