fruit = input()
day = input()
quantity = float(input())
work_days = ["Monday", " Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Sunday", "Saturday"]
fruits = ["banana", "apple", "orange", "grapefruit", " kiwi", "pineapple", " grapes"]
prices = [2.50, 1.20, 0.85, 1.45, 2.70, 5.50, 3.85]
weekend_prices = [2.70, 1.25, 0.90, 1.60, 3.00, 5.60, 4.20]

if fruit in fruits and day in work_days:
    cost_cases = zip(fruits, prices)
""" Think of a way for this to work!!!"""

else:
    print("error")