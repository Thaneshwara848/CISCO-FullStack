import mysql.connector
conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root",
        database="CISCO"
    )

cursor = conn.cursor();

empid = int(input("Enter Employee ID: "))

# Delete Employee
sql = "DELETE FROM Employee WHERE id = %s";

cursor.execute(sql, (empid,));

if cursor.rowcount > 0:
    print("Employee Deleted Successfully!")
else:
    print("Employee Not Found!")


cursor.close()
conn.close()
