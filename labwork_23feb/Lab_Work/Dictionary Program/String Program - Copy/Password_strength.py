# Password Strength Checker
# This program checks password strength
# Conditions:
# - At least 8 characters
# - Must contain a digit

password = input("Enter password: ")

has_digit = False

for ch in password:
    if ch.isdigit():
        has_digit = True

if len(password) >= 8 and has_digit:
    print("Strong Password")
else:
    print("Weak Password")
