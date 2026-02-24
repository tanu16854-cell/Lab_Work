# Program to validate username and password

# Predefined credentials
correct_username = "admin123"
correct_password = "pass@123"

# Taking input
username = input("Enter username: ")
password = input("Enter password: ")

# Checking login
if username == correct_username and password == correct_password:
    print("Login Successful")
else:
    print("Invalid Username or Password")
#OUTPUT
#Enter username: admin123
#Enter password: pass@123
#Login Successful
