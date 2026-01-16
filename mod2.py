def attendance_management():
    print("Attendence management")
    present_days = 0

    for day in range(1, 6):
        status = input(f"Day {day} Attendance (P/A): ").upper()
        if status == 'P':
            present_days += 1

    if present_days >= 4:
        attendance_status = "Regular"
    elif present_days == 3:
        attendance_status = "Warning"
    else:
        attendance_status = "Irregular"

    print("Total Present Days:", present_days)
    print("Attendance Status:", attendance_status)

    return present_days

attendance_management()
