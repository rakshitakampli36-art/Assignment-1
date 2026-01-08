emp_name=input("enter employee name: ")
salary=float(input("enter employeesalary : "))
rating=int(input("enter employee performance rating:5/4/3/2/1 : "))
if rating==5:
    bonus=salary*20/100
elif rating==4:
    bonus=salary*15/100
elif rating==3:
    bonus=salary*10/100
else:
    bonus=0
print("Empoyee name is : ",emp_name)
print("Employee's performance rating :",rating)
print("Bonus amount is: ",bonus)
final_salary=salary+bonus
print("Employee's final salary with bonus is: ",final_salary)
    
    
