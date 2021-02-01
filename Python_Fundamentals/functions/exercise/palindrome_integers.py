list_of_integers = input().split(", ")


def is_palindrome(lst_num_as_string):
    result = ""
    for number in lst_num_as_string:
        if number == number[::-1]:
            result = True
            print(result)
        else:
            result = False
            print(result)
    return exit()
print(is_palindrome(list_of_integers))