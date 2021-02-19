line = input().split()

list_of_words_as_char = []
new_word = []

# splits word in list of characters
def split_into_chars(a_word):
    current_word = []
    for char in a_word:
        current_word.append(char)
    return current_word

# finds the char according to asscii value
def what_char_is_it(word):
    first_letter = ""
    for char in word:
        if char.isnumeric():
            first_letter += char
    return chr(int(first_letter))

# finds digits in a list of characters and removes them
def remove_digits(word_as_list):
    word_with_letters = []
    for item in word_as_list:
        if item.isalpha():
            word_with_letters.append(item)
    return word_with_letters

# switches the places of second and last letter
def switch_places(word_as_list):
    result = word_as_list
    result[0], result[len(word_as_list) - 1] = result[len(word_as_list) - 1], result[0]
    return result

# joins the stings in each individual list
def join_string(word):
    complete_word = ""
    complete_word = "".join(word)
    return complete_word

complete_message = []

for i in range(len(line)):
    current_word = line[i]
    list_of_words_as_char.append(split_into_chars(current_word))
    first_char = what_char_is_it(current_word)
    new_word = switch_places(remove_digits(list_of_words_as_char[i]))
    new_word.insert(0, first_char)
    complete_message.append(join_string(new_word))
    final_message = " ".join(complete_message)

print(final_message)







# I also managed how to find the first letter of each word
# Now i have to find a way to replace the nummbers with the first letter
# So far I managed to split each word into a list of itch characters within a list
# Now i have to traverse each index of the big list