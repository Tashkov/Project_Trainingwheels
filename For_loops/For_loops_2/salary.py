n = int(input())
salary = float(input())

wage = salary

for i in range(n):
    website = input()
    if website == "Facebook":
        wage -= 150
    if website == "Instagram":
        wage -= 100
    if website == "Reddit":
        wage -= 50
    if wage == 0:
        print("You have lost your salary.")
        break

if wage == salary:
    print(round(salary))
elif 0 < wage != salary:
    print(round(wage))