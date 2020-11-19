n_moves = int(input())
score = 0
total_moves = 0
zero_nine = 0
ten_twenty = 0
twenty_thirty = 0
thirty_fourty = 0
fourty_fifty = 0
invalid_move = 0

for i in range(n_moves):
    n = int(input())
    total_moves += 1
    if n >= 0 and n <= 9:
        score += (n * 0.2)
        zero_nine += 1
    if 10 <= n <= 19:
        score += (n * 0.3)
        ten_twenty += 1
    if 20 <= n <= 29:
        score += (n * 0.4)
        twenty_thirty += 1
    if 30 <= n <= 39:
        score += 50
        thirty_fourty += 1
    if 40 <= n <= 50:
        score += 100
        fourty_fifty += 1
    if n > 50 or n < 0:
        score /= 2
        invalid_move += 1

p1 = zero_nine / total_moves * 100
p2 = ten_twenty / total_moves * 100
p3 = twenty_thirty / total_moves * 100
p4 = thirty_fourty / total_moves * 100
p5 = fourty_fifty / total_moves * 100
p6 = invalid_move / total_moves * 100

print(f'{score:.2f}\n'
      f'From 0 to 9: {p1:.2f}%\n'
      f'From 10 to 19: {p2:.2f}%\n'
      f'From 20 to 29: {p3:.2f}%\n'
      f'From 30 to 39: {p4:.2f}%\n'
      f'From 40 to 50: {p5:.2f}%\n'
      f'Invalid numbers: {p6:.2f}%')