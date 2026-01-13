num=int(input("enter a number"))
def fibb(num):
    if num==0:
        return 0
    elif num==1:
        return 1
    else:
        return fibb(num-1)+fibb(num-2)
for i  in range(num):
    print(fibb(i))

