def check_attendence(login_time):
    if login_time<="09:30":
        print("Present")
    elif "10:00">=login_time>"09:30":
        print("Late")
    else:
        print("Absent")
print(check_attendence("11:00"))
