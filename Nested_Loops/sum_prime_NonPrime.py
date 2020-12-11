num = input()

prime_numbers = 0
non_prime_numbers = 0

while num != "stop":
    num = int(num)
    if num < 0:
        print("Number is negative.")
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                non_prime_numbers += num
                break
        else:
            prime_numbers += num

    num = input()

print(f"Sum of all prime numbers is: {prime_numbers}\n"
      f"Sum of all non prime numbers is: {non_prime_numbers}")






