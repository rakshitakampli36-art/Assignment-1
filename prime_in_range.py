def prime_num(num):
    for i in range(1,num):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            print(i)
num=int(input("enter number"))
print("prime numbers are :",prime_num(num))
