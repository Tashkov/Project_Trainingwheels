import sys
n = int(input())

odd_sum = float(0)
even_sum = float(0)
odd_max = -sys.maxsize
even_max = -sys.maxsize
odd_min = sys.maxsize
even_min = sys.maxsize

if n == 0:
    print(f"OddSum={odd_sum:.2f},\nOddMin=No,\nOddMax=No,\n"
          f"EvenSum={even_sum:.2f},\nEvenMin=No,\nEvenMax=No")
elif n == 1:
    for i in range(1, n + 1):
        number = float(input())
        if i % 2 == 0:
            even_sum += number
            if number > even_max:
                even_max = number
            if number < even_min:
                even_min = number
            if odd_max == odd_max and odd_min == odd_min:
                print(f"OddSum={odd_sum:.2f},\nOddMin=No,\nOddMax=No,\n"
                      f"EvenSum={even_sum:.2f},\nEvenMin={even_min:.2f},\nEvenMax={even_max:.2f}")
        elif i % 2 != 0:
            odd_sum += number
            if number > odd_max:
                odd_max = number
            if number < odd_min:
               odd_min = number
            if even_max == even_max and even_min == even_min:
                print(f"OddSum={odd_sum:.2f},\nOddMin={odd_min:.2f},\nOddMax={odd_max:.2f},\n"
                      f"EvenSum={even_sum:.2f},\nEvenMin=No,\nEvenMax=No")
else:
    for i in range(1, n + 1):
        number = float(input())
        if i % 2 == 0:
            even_sum += number
            if number > even_max:
                even_max = number
            if number < even_min:
                even_min = number
        elif i % 2 != 0:
            odd_sum += number
            if number > odd_max:
                odd_max = number
            if number < odd_min:
                odd_min = number
    print(f"OddSum={odd_sum:.2f},\nOddMin={odd_min:.2f},\nOddMax={odd_max:.2f},\n"
          f"EvenSum={even_sum:.2f},\nEvenMin={even_min:.2f},\nEvenMax={even_max:.2f}")
