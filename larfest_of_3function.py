def largest_of_3(a,b,c):
    if a>b:
        print("a is largest")
        if a>c:
            print("a is largest")
        else:
            print("c is largest")
    else:
        if b>c:
            print("b is largest")
        else:
            print("c is larest")
a=int(input("enter first number :"))
b=int(input("enter second number :"))
c=int(input("enter third number :"))
largest_of_3(a,b,c)

