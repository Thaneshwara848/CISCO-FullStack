
import mysql.connector

# MySQL Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="CISCO"
)

cursor = conn.cursor()

# Create Employee Table
cursor.execute("""
CREATE TABLE IF NOT EXISTS Employee (
    id INT PRIMARY KEY,
    name VARCHAR(100),
    age INT,
    salary DOUBLE,
    desig VARCHAR(100)
)
""")

conn.commit()

while True:

    print("\n====== EMPLOYEE MANAGEMENT ======")
    print("1. Add Employee")
    print("2. View All Employees")
    print("3. Search Employee")
    print("4. Update Salary")
    print("5. Delete Employee")
    print("6. Exit")
    print("=================================")

    choice = input("Enter Your Choice: ")

    if choice == "6":
        print("Thank You!")
        break

    try:
        # CREATE
        if choice == "1":

            empid = int(input("Enter Employee ID: "))
            name = input("Enter Employee Name: ")
            age = int(input("Enter Employee Age: "))
            salary = float(input("Enter Salary: "))
            desig = input("Enter Designation: ")

            if empid <= 0 or age <= 0 or salary <= 0:
                raise ValueError("ID, Age and Salary must be positive")

            if not name.strip() or not desig.strip():
                raise ValueError("Name and Designation cannot be empty")

            sql = """
            INSERT INTO Employee (id, name, age, salary, desig)
            VALUES (%s, %s, %s, %s, %s)
            """

            cursor.execute(
                sql, (empid, name, age, salary, desig)
            )

            conn.commit()
            print("Employee Added Successfully!")

        # READ ALL
        elif choice == "2":

            sql = "SELECT * FROM Employee"
            cursor.execute(sql)

            employees = cursor.fetchall()

            if len(employees) == 0:
                print("No Employees Found!")
            else:
                for emp in employees:
                    print("ID:", emp[0])
                    print("Name:", emp[1])
                    print("Age:", emp[2])
                    print("Salary:", emp[3])
                    print("Designation:", emp[4])
                    print("-------------------------")

        # SEARCH BY ID
        elif choice == "3":

            empid = int(input("Enter Employee ID: "))

            sql = "SELECT * FROM Employee WHERE id = %s"

            cursor.execute(sql, (empid,))
            emp = cursor.fetchone()

            if emp:
                print("Employee Found:", emp)
            else:
                print("Employee Not Found!")

        # UPDATE SALARY
        elif choice == "4":

            empid = int(input("Enter Employee ID: "))
            salary = float(input("Enter New Salary: "))

            if salary <= 0:
                raise ValueError("Salary must be positive")

            sql = """
            UPDATE Employee
            SET salary = %s
            WHERE id = %s
            """

            cursor.execute(sql, (salary, empid))
            conn.commit()

            if cursor.rowcount > 0:
                print("Salary Updated Successfully!")
            else:
                print("Employee Not Found or Salary Unchanged!")

        # DELETE EMPLOYEE
        elif choice == "5":

            empid = int(input("Enter Employee ID: "))

            sql = "DELETE FROM Employee WHERE id = %s"

            cursor.execute(sql, (empid,))
            conn.commit()

            if cursor.rowcount > 0:
                print("Employee Deleted Successfully!")
            else:
                print("Employee Not Found!")

        else:
            print("Invalid Choice! Please select 1 to 6.")

    except ValueError as error:
        print("Input Error:", error)

    except mysql.connector.Error as error:
        conn.rollback()
        print("Database Error:", error)

cursor.close()
conn.close()
