strawberry_price = float(input())
net_bannanas_kg = float(input())
net_oranges_kg = float(input())
net_raspberries_kg = float(input())
net_strawberries_kg = float(input())

""" Here store the prices"""
raspberries_price = strawberry_price / 2
oranges_price = raspberries_price - (0.4*raspberries_price)
banannas_price = raspberries_price - (0.8*raspberries_price)

""" Here we store the sum total prices """
raspberries_sumtotal = raspberries_price*net_raspberries_kg
oranges_sumototal = oranges_price*net_oranges_kg
banannas_sumtotal = banannas_price*net_bannanas_kg
strawberry_sumtotal = strawberry_price*net_strawberries_kg

total_price = raspberries_sumtotal + oranges_sumototal +banannas_sumtotal +strawberry_sumtotal

print(total_price)