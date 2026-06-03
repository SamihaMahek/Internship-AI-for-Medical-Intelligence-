#Create a Python program that checks password strength and displays whether it is Weak, Medium, or Strong.
password = input("Enter your password: ")

length = len(password)

has_upper = False
has_lower = False
has_digit = False
has_special = False

special_chars = "!@#$%^&*()_+-=[]{}|;:',.<>?/"
for ch in password:
    if ch.isupper():
        has_upper = True
    elif ch.islower():
        has_lower = True
    elif ch.isdigit():
        has_digit = True
    elif ch in special_chars:
        has_special = True

score = 0

if length >= 8:
    score += 1
if has_upper:
    score += 1
if has_lower:
    score += 1
if has_digit:
    score += 1
if has_special:
    score += 1

if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")