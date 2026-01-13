num=int(input("enter a number"))
count=0
while num!=0:
    num=num//10
    count+=1
print("number of digits in a entered number is :",count)
