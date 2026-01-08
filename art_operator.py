amount=float(input("enter the price of product"))
gst=amount*18/100
final_amt=amount+gst
print("final amount is : ",final_amt)

no_student=int(input("enter number of students : "))
member_in_group=int(input("enter number o groups to divide : "))
no_of_groups=no_student%member_in_group
print("equal number of groups are : ",no_of_groups)


voltage=int(input("enter the voltage used :"))
current=int(input("enter the rate o current :"))
power=voltage*current 
power_consumption=power*(10**-3)
print("power consumption is :",power_consumption)

