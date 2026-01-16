def login(username, password):
    if username == "dd_admin" and password == "dd@123":
        print("Login Successful ")
    else:
        print("Access Denied")
print("Digital Dreams Login")
user = input("Enter Username: ")
pwd = input("Enter Password: ")

login(user, pwd)
   
