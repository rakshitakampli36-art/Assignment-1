employee_name=input("enter employee name")
employee_id=input("enter employee id")
basic_salary=float(input("enter employee salary"))
har=0.20*basic_salary
da=0.10*basic_salary
pf=0.12*basic_salary
net_salary=basic_salary+har+da-pf
print("Employee name is:",employee_name)
print("Employee id is:",employee_id)
print("Employee basic salary is:",basic_salary)
print("HAR = ",har)
print("DA = ",da)
print("PF = ",pf)
print("Net salary of an employee is ",net_salary)
 
