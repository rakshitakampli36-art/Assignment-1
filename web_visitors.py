
visitors=list(map(int,input("Enter number of visitors of week").split()))
print(visitors)
if len(visitors)!=7:
    print("Enter only 7 days visitors")
else:
    high_traffic=max(visitors)
    high_day_idx=visitors.index(high_traffic)
    high_day=high_day_idx+1

    lower_traffic=min(visitors)
    low_day_idx=visitors.index(lower_traffic)
    low_day=low_day_idx+1

    print("Highest traffic is :",high_traffic)
    print("Highest traffic is on day :",high_day)

    print("Lower traffic is :",lower_traffic)
    print("Lower traffic is :",low_day)


    




























