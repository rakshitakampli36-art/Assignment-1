scores=[65,25,68,30,91,50,78,49]
print(scores)
print("Total score is :",sum(scores))
avg=sum(scores)/len(scores)
print("Average score is :",avg)
above_avg=0
for score in scores:
    if score>avg:
        above_avg+=1
               
print("count of scores above average is",above_avg)
