import sys


MASTER_PASSWORD = 'opensame'
password = input("Please enter the super secret password:  \n")
attempt_count = 1
while password != MASTER_PASSWORD:
    if attempt_count > 3:
        sys.exit("Too many invalid password attempts")
    password = input("Invalid password, try again: \n")
    attempt_count += 1
print("Welcom to secret village")