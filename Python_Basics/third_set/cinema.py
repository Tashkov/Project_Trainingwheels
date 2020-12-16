movie = input()
rows = int(input())
columns = int(input())
'''Types of movies'''
premiere = 12.00
normal = 7.50
discount = 5.00
full_cinema = rows * columns

if movie == "Premiere":
    print(f'{full_cinema * premiere:.2f}')
elif movie == "Normal":
    print(f'{full_cinema * normal:.2f}')
elif movie == "Discount":
    print(f'{full_cinema * discount:.2f}')