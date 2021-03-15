first_word, second_word = input().split()
sum_total = 0

if len(first_word) == len(second_word):
    for index in range(0, len(first_word)):
        first_num = int(ord(first_word[index]))
        second_num = int(ord(second_word[index]))
        sum_total += first_num * second_num

elif len(first_word) > len(second_word):
    remaining_letters = len(first_word) - len(second_word)
    for index in range(0, len(second_word)):
        first_num = int(ord(first_word[index]))
        second_num = int(ord(second_word[index]))
        sum_total += first_num * second_num
    for i in range(-1, -(remaining_letters + 1), -1):
        sum_total += int(ord(first_word[i]))
else:
    remaining_letters = len(second_word) - len(first_word)
    for index in range(0, len(first_word)):
        first_num = int(ord(second_word[index]))
        second_num = int(ord(first_word[index]))
        sum_total += first_num * second_num
    for i in range(-1, -(remaining_letters + 1), -1):
        sum_total += int(ord(second_word[i]))

print(sum_total)
