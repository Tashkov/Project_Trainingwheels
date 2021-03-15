text = input()
encrypted_word = ""

for char in text:
    new_char = chr(int(ord(char))+3)
    encrypted_word += new_char
print(encrypted_word)