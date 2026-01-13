def simple_intrest(p,t,r):
    si=p*t*r/100
    return si
p=float(input("Enter price :"))
t=int(input("Enter time :"))
r=float(input("Enter rate of intreat :"))
print("simple intrest is:",simple_intrest(p,t,r))
