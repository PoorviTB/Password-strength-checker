import re

password = input("Enter your password: ")

# Check different conditions
length = len(password) >= 8
uppercase = re.search("[A-Z]", password)
lowercase = re.search("[a-z]", password)
number = re.search("[0-9]", password)
special = re.search("[!@#$%^&*]", password)

# Check password strength
if length and uppercase and lowercase and number and special:
    print("Password Strength: Strong")
elif length and uppercase and lowercase and number:
    print("Password Strength: Medium")
else:
    print("Password Strength: Weak")