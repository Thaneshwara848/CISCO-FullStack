employee = {
    "name":"Thanesh",
    "age":25,
    "Salary":50000
}

print(employee)

print("================== : " ,  employee["Salary"])
employee.update({"age":26});
print(employee)

employee.update({"Designation":"Manager"});
print(employee);


print("==============KEYS+===========")

print(employee.keys());

print("==============VALUES+===========")

print(employee.values());

employee.clear();

print(employee);