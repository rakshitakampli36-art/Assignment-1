name=input("enter name")
age=int(input("enter age"))
email=input("enter email")
contact=input("enter contact details")
percentage=float(input("enter percentage"))
if age<18:
    print(" Invalid age must be greater then 18")
elif percentage<60:
    print("Invalid precentage must be greater then 60%")
elif contact!=10:
    print("Invalid contact number should equal to 10")
else:
    print("Intern eligible for internship")
