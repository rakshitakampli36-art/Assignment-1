def vowels_const(a):
    a.lower()
    vow=0
    const=0
    for i in a:
        if i in ['a','e','i','o','u']:
            vow+=1
        else:
             const+=1
    print("vowels in string are :",vow)
    print("consonents in string are :",const)
a=input("enter string: ")
vowels_const(a)
