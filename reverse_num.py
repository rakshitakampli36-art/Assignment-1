n=int(input("Enter a number to be reversed"))
rev=0
while n!=0:
    m=n%10 
    rev=(rev*10)+m
    n=n//10
print("reversed number is :",rev)
