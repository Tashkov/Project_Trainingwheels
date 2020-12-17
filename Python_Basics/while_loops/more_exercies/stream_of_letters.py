import string
line = input()  # The user must input only letters from the latin alphabet

secret_word = "con"
secret_counter = 0
temp_word = ""
word = ""

while line != "End":
    if line in secret_word:
        secret_counter += 1
        secret_word = secret_word.replace(line,"")
        if secret_counter % 3 == 0:  # the logic for the secret word
            word += temp_word
            word += " "
            secret_word = "con"
            temp_word = ""
            line = input()
        else:
            line = input()
    elif line not in string.ascii_letters:  # checks whether there is a symbol
        line = input()
    else:
        temp_word += line
        line = input()

print(word)