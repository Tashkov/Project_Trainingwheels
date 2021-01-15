from itertools import permutations
number = input()

list_of_numbers = []
list_of_ints = []

# takes the input str of number and inserts each integer as a different index in the list_of_numbers
for i in range(len(number)):
    list_of_numbers.append(int(number[i]))

perm = permutations(list_of_numbers)
for i in perm:
    list_of_ints.append(i)
    print(i)
print(list_of_ints)

#You`re half way there. Find out how to convert the indexes from each tuple into an integer

