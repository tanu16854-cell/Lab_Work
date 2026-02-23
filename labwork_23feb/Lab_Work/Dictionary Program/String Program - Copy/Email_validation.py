# Email Validation System
# This program checks if email is valid
# Conditions:
# - Must contain '@' and '.'

email = input("Enter email: ")

if "@" in email and "." in email:
    print("Valid Email")
else:
    print("Invalid Email")
