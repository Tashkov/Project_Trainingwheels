width = int(input())
length = int(input())
whole_cake = width * length
taken = 0

while True:
    piece = input()
    if piece == "STOP":
        print(f"{whole_cake - taken} pieces are left.")
        break
    taken += int(piece)
    if taken > whole_cake:
        print(f"No more cake left! You need {taken - whole_cake} pieces more.")
        break
