vegetable_price = float(input())
fruit_price = float(input())
vegetable_net_weight = int(input())
fruit_net_weight = int(input())

profit = ((vegetable_price * vegetable_net_weight) + (fruit_price*fruit_net_weight)) / 1.94

print(f'{profit:.2f}')

