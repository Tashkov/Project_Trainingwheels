room_rent = int(input())

cake_price = (room_rent * 20)/100
drinks_price = cake_price-(cake_price * 45)/100
clown_price = room_rent / 3

total_price = room_rent+cake_price+drinks_price+clown_price
print(total_price)
