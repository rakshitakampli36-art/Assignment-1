num=int(input("enter a number "))
fact=1
if num<=0:
    print("enter positive number")
else:
    for i in range(1,num+1):
        fact=fact*i
print("Factorial of given number is :",fact)
