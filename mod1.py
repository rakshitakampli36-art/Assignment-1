def register_employee():
    print("Employee Registration")
    
    emp_id = input("Enter Employee ID: ")
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    department = input("Enter Department: ")
    basic_salary = float(input("Enter Basic Salary: "))

    if age < 18:
        print("Error Age must be 18 or above")
        return None
    if basic_salary <= 0:
        print("Error Salary must be greater than 0")
        return None

    print("Employee Registered Successfully")

    return emp_id, name, age, department, basic_salary
print(register_employee())
