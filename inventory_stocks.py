open_stock=[89,76,132,128]
close_stock=[65,79,87,253]
for i in range(len(open_stock)):
    if close_stock[i]>open_stock[i]:
        print(f"Product {i+1}:Closing Stock is Increased")
    elif open_stock[i]>close_stock[i]:
        print(f"Product {i+1}: Closing Stock is Decreased")
    else:
        print(f"Product {i+1}:No Changes in opening and closing stock")
