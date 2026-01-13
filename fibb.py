num=int(input("enter a number : "))
print("Fibbonacci series is :")
n1=0
n2=1
count=0
print(n1)
print(n2)
while num>0:
    result=n1+n2
    n1=n2
    n2=result
    num=num-1
    print(result)
