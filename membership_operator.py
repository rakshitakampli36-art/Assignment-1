attendance_list=input("enter list of students: ").split()
student=input("enter name of student : ")

if student not in attendance_list:
    print("invalid student")
else:
    print("student is present")




list_of_products=input("enter list of products : ").split()
product_to_check=input("enter products to be searched : ")
if product_to_check in list_of_products:
    print("Product is available")
else:
    print("Product is not avaiable")
