import sys
n = int(input())

odd_sum = float(0)
even_sum = float(0)

odd_max = 0
even_max = 0
odd_min = 0
even_min = 0

for i in range(1, n + 1):
    number = float(input())
    if i == 1:
        odd_max = odd_min = number
    if i == 2:
        even_max = even_min = number
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

if odd_max == 0 and odd_min == 0 and even_max == 0 and even_min == 0:
    print(f"OddSum={odd_sum:.2f},\nOddMin=No,\nOddMax=No,\n"
              f"EvenSum={even_sum:.2f},\nEvenMin=No,\nEvenMax=No")
elif odd_max == 0 and odd_min == 0 :
    print(f"OddSum={odd_sum:.2f},\nOddMin=No,\nOddMax=No,\n"
              f"EvenSum={even_sum:.2f},\nEvenMin={even_min:.2f},\nEvenMax={even_max:.2f}")
elif even_max == 0 and even_min == 0:
    print(f"OddSum={odd_sum:.2f},\nOddMin={odd_min:.2f},\nOddMax={odd_max:.2f},\n"
          f"EvenSum={even_sum:.2f},\nEvenMin=No,\nEvenMax=No")
else:
    print(f"OddSum={odd_sum:.2f},\nOddMin={odd_min:.2f},\nOddMax={odd_max:.2f},\n"
          f"EvenSum={even_sum:.2f},\nEvenMin={even_min:.2f},\nEvenMax={even_max:.2f}")
        