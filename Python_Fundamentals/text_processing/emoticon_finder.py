text = input()
emoticon = ""
for index in range(0, len(text)):
    if text[index] == chr(58):
        emoticon += text[index]
        next_letter = text[index + 1]
        if 33 <= ord(next_letter) <= 126:
            emoticon += next_letter
            print(emoticon)
            emoticon = ""
