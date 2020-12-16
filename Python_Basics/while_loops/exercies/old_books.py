book_name = input()
book_count = 0

while True:
    books = input()
    if books == book_name:
        print(f'You checked {book_count} books and found it.')
        break
    if books == "No More Books":
        print(f'The book you search is not here!\n'
              f'You checked {book_count} books.')
        break
    book_count += 1