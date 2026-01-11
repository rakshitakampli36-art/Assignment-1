distance=float(input("enter distance in kilo meters"))
if distance<=5:
    print("Local")
elif 6<=distance<=20:
    print("City")
else:
    print("Outstation")
