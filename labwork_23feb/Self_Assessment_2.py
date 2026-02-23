# -------------------------------------------------------
# ------------STRING SELF-ASSESSMENT PROJECT-------------------
# GROCERY BILL INPUT VALIDATION SYSTEM
# -------------------------------------------------------

print("===== Grocery Store Billing System =====\n")

# -------- NAME INPUT --------
name = input("Enter your name: ")

# Remove extra spaces
name = name.strip()

# Validate name (only alphabets allowed)
if not name.replace(" ", "").isalpha():
    print("Invalid Name! Only alphabets allowed.")
else:
    print("Valid Name:", name.title())


# -------- MOBILE NUMBER --------
mobile = input("\nEnter your mobile number: ")

# Validate mobile number (only digits and length = 10)
if mobile.isdigit() and len(mobile) == 10:
    print("Valid Mobile Number")
else:
    print("Invalid Mobile Number!")


# -------- COUPON CODE --------
coupon = input("\nEnter coupon code: ")

# Remove spaces
coupon = coupon.strip()

# Check if coupon is alphanumeric
if coupon.isalnum():
    
    # Check case conditions
    if coupon.isupper():
        print("Coupon Applied Successfully (Uppercase Code)")
    elif coupon.islower():
        print("Coupon Applied Successfully (Lowercase Code)")
    else:
        print("Coupon Applied (Mixed Format)")
else:
    print("Invalid Coupon Code! Only letters and numbers allowed.")


# -------- FINAL MESSAGE --------
print("\n===== Thank You for Visiting Grocery Store =====")
