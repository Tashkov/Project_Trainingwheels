line1 = list(map(lambda x: int(x), input().split()))
line2 = list(map(lambda x: int(x), input().split()))
line3 = list(map(lambda x: int(x), input().split()))

board = [line1, line2, line3]
# rows first player
if board[0][0] == board[0][1] == board[0][2] == 1:
    print("First player won")
elif board[1][0] == board[1][1] == board[1][2] == 1:
    print("First player won")
elif board[2][0] == board[2][1] == board[2][2] == 1:
    print("First player won")
# rows second player
elif board[0][0] == board[0][1] == board[0][2] == 2:
    print("Second player won")
elif board[1][0] == board[1][1] == board[1][2] == 2:
    print("Second player won")
elif board[2][0] == board[2][1] == board[2][2] == 2:
    print("Second player won")
# columns first player
elif board[0][0] == board[1][0] == board[2][0] == 1:
    print("First player won")
elif board[0][1] == board[1][1] == board[2][1] == 1:
    print("First player won")
elif board[0][2] == board[1][2] == board[2][2] == 1:
    print("First player won")
# columns second player
elif board[0][0] == board[1][0] == board[2][0] == 2:
    print("Second player won")
elif board[0][1] == board[1][1] == board[2][1] == 2:
    print("Second player won")
elif board[0][2] == board[1][2] == board[2][2] == 2:
    print("Second player won")
# diagonal first player
elif board[0][0] == board[1][1] == board[2][2] == 1:
    print("First player won")
elif board[0][2] == board[1][1] == board[2][0] == 1:
    print("First player won")
# diagonal second player
elif board[0][0] == board[1][1] == board[2][2] == 2:
    print("Second player won")
elif board[0][2] == board[1][1] == board[2][0] == 2:
    print("Second player won")
else:
    print('Draw!')