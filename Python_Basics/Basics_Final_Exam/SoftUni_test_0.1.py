price_per_page = float(input())
price_per_cover = float(input())
percent_discount_paper = int(input())
wage_designer = float(input())
team_participation_money = int(input())

book_pages = 899
book_covers = 2

book_price = ((book_pages * price_per_page) + (book_covers * price_per_cover))
paper_discount = book_price  * (percent_discount_paper / 100)
book_price_new = (book_price - paper_discount) + wage_designer
team_participation = book_price_new * (team_participation_money / 100)
total_price = book_price_new - team_participation

print(f"Avtonom should pay {total_price:.2f} BGN.")