h_meters = float(input())
w_meters = float(input())


"""conversion to cm"""

h = h_meters * 100
w = w_meters * 100


""""calculations per work space:
one workspace is 70 cm wide and 120 cm long
the corridor is 100cm wide
door and teacher workspace take 3 workspaces"""

len_deduction = h // 120
width_deduction = (w - 100) // 70

total = int((len_deduction * width_deduction) - 3)

print(total)