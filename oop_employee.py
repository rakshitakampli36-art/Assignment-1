class Employee:
    def __init__(self,name,age,salary,gender):
        self.name=name
        self.age=age
        self.salary=salary
        self.gender=gender
    def emp_detailes(self):
        print("Employee name is:",self.name)
        print("Employee's age is:",self.age)
        print("Employee's salary is:",self.salary)
        print("Employee's gender is:",self.gender)
e1=Employee("sam",32,85000,"Male")
e1.emp_detailes()
