def longer_line(x1,y1,x2,y2,x3,y3,x4,y4):
    if sum([(x1), (y1), (x2), (y2)]) <= sum([(x3), (y3), (x4), (y4)]):
        if sum([abs(x1), abs(y1)]) <= sum([abs(x2), abs(y2)]):
            q = (x, y) = (int(x1), int(y1))
            z = (a, b) = (int(x2), int(y2))

        else:
           q = (x, y) = (int(x2), int(y2))
           z = (a, b) = (int(x1), int(y1))

    else:
        if sum([abs(x3), abs(y3)]) <= sum([abs(x4), abs(y4)]):
            q = (x, y) = (int(x3), int(y3))
            z = (a, b) = (int(x4), int(y4))

        else:
            q = (x, y) = (int(x4), int(y4))
            z = (a, b) = (int(x3), int(y3))
    return f"{q}{z}"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())

print(longer_line(x1,y1,x2,y2,x3,y3,x4,y4))