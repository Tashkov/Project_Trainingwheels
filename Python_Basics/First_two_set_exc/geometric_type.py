import math

geometric_shape = str(input())

if geometric_shape == "square":
    side_lenght = float(input())
    square_face = round((side_lenght*side_lenght), 3)
    print (square_face)
elif geometric_shape == "rectangle":
    side_lenght_one = float(input())
    side_lenght_two = float(input())
    rectangle_face = round ((side_lenght_one*side_lenght_two), 3)
    print (rectangle_face)
elif geometric_shape == "circle":
    radius = float(input())
    circle_face = round(((radius*radius) * math.pi), 3)
    print (circle_face)
elif geometric_shape == "triangle":
    side_lenght_triangle = float(input())
    height_triangle = float(input())
    triangle_face = round (((side_lenght_triangle*height_triangle) / 2), 3)
    print (triangle_face)