from fastapi import FastAPI
app= FastAPI();
from pydantic import BaseModel
                                    # API --- also we call as End Point ----------- RESt API : 
@app.get("/")
def home():
    return {"message":"Hello Welcome to HOME PAGE "}

class Employee(BaseModel)  :              
    id :int 
    name :str
    age :int 
    salary :float 
    desig :str 

employees = [] ; 
@app.post("/addEmployee")
def addEmployee(emps : Employee ):
    employees.append(emps);           
    return {"message" : "Employee Added Succssfully...!"}
@app.get("/getAllEmployee")
def getAllEmployee():
    #get all employee logic
    return employees;
@app.get("/employeeByID/{id}")
def  getEmployeeByID(id: int):
    for emp in employees:
        if emp.id == id:
            return emp
    return {"message": "Employee Not Found"}

@app.delete("/deleteEmployee/{id}")
def deleteEmployee(id: int):
    for emp in employees:
        if emp.id == id:
            employees.remove(emp)
            return {"message": "Employee Deleted Successfully"}
    return {"message": "Employee Not Found"}

@app.delete("/deleteAllEmployees")
def deleteAllEmployees():
    employees.clear()
    return {"message": "All Employees Deleted Successfully"}

@app.put("/updateEmployee/{id}")
def updateEmployee(id: int, updatedEmp: Employee):
    for emp in employees:
        if emp.id == id:
            emp.name = updatedEmp.name
            emp.age = updatedEmp.age
            emp.salary = updatedEmp.salary
            emp.desig = updatedEmp.desig
            return emp

    return {"message": "Employee Not Found"}


#FastAPI – Employee CRUD APIs
#No.	    Method      	Endpoint	            Description
#1	        POST	        /addEmployee	        Add new employee
#2	        GET	            /getAllEmployee	        Get all employees
#3	        GET	            /employeeByID/{id}	    Get employee by ID
#4	        PUT	            /updateEmployee/{id}	Update employee by ID
#5	        DELETE         	/deleteEmployee/{id}	Delete employee by ID
#6	        DELETE	        /deleteAllEmployees	    Delete all employees