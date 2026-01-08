def check_eligibility(age,percentage):
    if age>=18:
        if percentage>=60:
            print("Eligible")
        else:
            print("Not eligible")
    else:
       print("Not eligible")
age=int(input("enter your age"))
percentage=float(input("enter your percentage"))
check_eligibility(age,percentage)
