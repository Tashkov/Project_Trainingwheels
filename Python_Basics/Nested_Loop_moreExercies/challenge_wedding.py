male_customers = int(input())  # int btw 1 - 100
female_customers = int(input())  # int btw 1 - 100
tables = int(input())  # int btw 1 - 100

counter = 0

for male in range(1, male_customers + 1):
    for female in range(1, female_customers + 1):
        if counter == tables:
            break
        else:
            counter += 1
            print(f"({male} <-> {female})", end=" ")
