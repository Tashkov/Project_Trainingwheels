n = int(input())
big_board = []

def finding_ones_horizontally(big_list):
    check = 0
    for i in range(0, n):
        for i_digit in range(0, n):
            i_digit2 = i_digit + 1
            if big_list[i][i_digit] == big_list[i][i_digit2] == 1:
                check += 1
    if check >= 2:
        return True

def finding_ones_vertically(big_list):
    check = 0
    for i_row1 in range(0, n):
        i_row2 = i_row1 + 1
        for i_digit in range(0, n):
            i_digit2 = i_digit + 1
            if big_list[i_row1][i_digit] == big_list[i_row2][i_digit2] == 1:
                check += 1
    if check >= 2:
        return True


for times in range(1, n + 1):
    line = list(map(lambda x: int(x), input().split()))
    big_board.append(line)
    looking_for_ones = [digit for digit in line if digit == digit and digit == 1]


x = finding_ones_vertically(big_board)

print(big_board)