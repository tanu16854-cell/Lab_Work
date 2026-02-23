# User Registration System
# This program checks if username is valid
# Conditions:
# - Length must be at least 5 characters
# - No spaces allowed

username = input("Enter username: ")

if len(username) >= 5 and " " not in username:
    print("Valid Username")
else:
    print("Invalid Username")
