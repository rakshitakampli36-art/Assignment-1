def calc_dis(price,customer_type):
    if customer_type=="Regular":
        discount=price*5/100
        print("final_price is",price-discount)
    elif customer_type=="Premium":
        discount=price*15/100
        print("final_price is",price-discount)
    elif customer_type=="Emloyee":
        discount=price*25/100
        print("final_price is",price-discount)
price=int(input("enter price :"))
customer_type=input("eneter customer type :")
calc_dis(price,customer_type)
