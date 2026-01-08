def electric_bill(units):
    bill=0
    if units<=100:
        bill=units*2
    elif units<=200:
        bill=(100*2)+((units -100)*4)
    elif units>200:
        bill=(100*2)+(100*4)+((units -200)*6)
    return bill
units=int(input("eneter number of units "))
totalbill=electric_bill(units)
print(totalbill)

