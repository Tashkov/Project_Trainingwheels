n = int(input())  # int > 0

print("+ " + (n - 2) * "- " + "+")

for i in range(n - 2):
    print("| " + (n - 2) * "- " + "|")

print("+ " + (n - 2) * "- " + "+")
