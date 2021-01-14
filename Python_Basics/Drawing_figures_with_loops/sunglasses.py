n = int(input())  # 3 <= n <= 100

print((2*n) * "*" + n * " " + (2*n) * "*")
for i in range(1, (n - 1)):
    if i == (n - 1) / 2 - 1:
        print("*" + (2*(n-1)) * "/" + "*" + n * "|" + "*" + 2*(n-1)*"/" + "*")
    else:
        print("*" + (2 * (n - 1)) * "/" + "*" + n * " " + "*" + 2 * (n - 1) * "/" + "*")
print((2*n) * "*" + n * " " + (2*n) * "*")

# finish the logic in the if - else statement so that it works properly