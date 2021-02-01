line_words = input()
palindrome = input()
counter = 0
words = line_words.split()
lst_palindromes = []
# checks if a word is palindrome or not
def isPalindrome(s):
    return s == s[::-1]

for word in words:
    if isPalindrome(word):
        lst_palindromes.append(word)
    else:
        continue

for index in range(len(lst_palindromes)):
    if lst_palindromes[index] == palindrome:
        counter += 1
    else:
        continue

print(lst_palindromes)
print(f'Found palindrome {counter} times')