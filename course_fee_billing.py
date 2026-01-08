course=input("enter course")
if course=="Python":
    fees=5000
elif course=="Data Analytics":
    fees=8000
elif course=="AI & ML":
    fees=12000
else:
    print("Invalid Course")
    exit()
student=input("is regular student :YES/NO")
early=input("early registration : YES/NO")
if student=="YES":
    discount=fees*10/100
if early=="YES":
    discount=fees*15/100
final_amount=fees-discount
print("course name= ",course)
print("Original fees= ",fees)
print("Discount amount= ",discount)
print("Final payment amount= ",final_amount)
