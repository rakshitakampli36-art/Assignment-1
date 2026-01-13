def palindrome(n):
    if n==n[::-1]:
        print("Number is palindrome")
    else:
        print("Number is not a palindrome")

n=input("enter a number")
palindrome(n)
