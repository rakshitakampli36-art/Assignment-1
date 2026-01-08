def check_password(password):
  if len(password)<8:
    print("Weak Password\nNumber of character is less than 8")
  special_char="!@#$%^&*()_+=-{}[]:'<>?/~"
  special=any(i in special_char for i in password)
  digit=any(i.isdigit() for i in password)
  if len(password)>=8 and digit and special:
    print("Strong Password")
  else:
    print("Password must contain a digit and special character")
password=input("Enter a Password")
check_password(password)
