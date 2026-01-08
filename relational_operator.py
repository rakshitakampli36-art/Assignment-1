age=int(input("enter the age of voter :"))
if age>=18:
    print("eligible to vote")
else:
    print("not eligible to vote")


emp_1_salary=float(input("enter the salary of employee 1"))
emp_2_salary=float(input("enter the salary of employee 2"))
emp_3_salary=float(input("enter the salary of employee 3"))
if emp_1_salary>emp_2_salary:
    if emp_1_salary>emp_3_salary:
        print("Employee 1 earns more")
    else:
        print("Employee 3 earns more")
else:
    if emp_2_salary>emp_3_salary:
        print("Employee 2 earns more")
    else:
        print("Employee 3 earns more")
    

login_pin=1122334
entered_pin=input("enter login pin :")
if entered_pin == login_pin:
    print("login pin varifed")
else:
    print("Password incorrect")
    















































