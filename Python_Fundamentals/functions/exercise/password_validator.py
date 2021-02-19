# recive a single line
line = input()

# declare a function named password_validator
def password_validator(pass_word):
    password = pass_word
    rule1 = False
    rule2 = False
    rule3 = False
    # check if the length is btw 6 - 10 char inclusive
    if 6 <= len(password) <= 10:
        rule1 = True
    # check if the password conssist only of lettets and digits
    if password.isalnum():
        rule2 = True
    # checks if the password has at least 2 digits
    counter = 0
    for char in password:
        if char.isnumeric():
            counter += 1
    if counter >= 2:
        rule3 = True
    if rule1 and rule2 and rule3:
        return "Password is valid"
    if not rule1:
        print("Password must be between 6 and 10 characters")
    if not rule2:
        print("Password must consist only of letters and digits")
    if not rule3:
        print("Password must have at least 2 digits")
    return exit()

print(password_validator(line))