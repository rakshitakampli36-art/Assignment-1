def calculate_salary(basic_salary, present_days):
    PF = basic_salary * 0.12
    if present_days < 3:
        HRA = 0
        DA = 0
    else:
        HRA = basic_salary * 0.20
        DA = basic_salary * 0.10
        net_salary = basic_salary + HRA + DA - PF
        print(net_salary)
salary=float(input("enter basic salary of employee"))
present_day=int(input("enter number of days present"))
calculate_salary(salary,present_day)

