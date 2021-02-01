electrons = int(input())

atom = []
index = 0
n = 1
while electrons != 0:
    amount = 2*n**2
    if amount > electrons:
        atom.append(electrons)
        break
    else:
        atom.append(amount)
        electrons -= amount
        index += 1
        n += 1

print(atom)
