text = input()

while not text == "end":
    word = text
    word_as_list = word
    reversed_text = "".join([text[i] for i in range(-1, -(len(text)+1), -1)])
    print(f"{word} = {reversed_text}")

    text = input()
