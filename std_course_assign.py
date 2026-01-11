students={"Asha":"Pyton","Ravi":"Data Analytics","Neha":"AI"}
print(students)
print("Students name are:",students.keys())
print("Courses enrolled are:",students.values())
std=input("enter a student name to check")
if std in students:
    print("student is present")
else:
    print("student is not present")
    
