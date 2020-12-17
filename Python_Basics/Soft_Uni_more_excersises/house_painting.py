x = float(input())
y = float(input())
h = float(input())

""" Faces of the parts of the house in green"""
entrance = (x * x) - (1.2 *2)
side_window = ((x * y) - (1.5 * 1.5)) * 2
back = x * x
total_green = entrance + side_window + back

""" Faces of the parts of the house in red"""
red_side = (x * y) * 2
red_triangle = ((x * h) / 2 ) * 2
total_red = red_side + red_triangle

""" total paint"""
green_paint = total_green / 3.4
red_paint = total_red / 4.3

print(f'{green_paint:.2f} \n{red_paint:.2f}')

