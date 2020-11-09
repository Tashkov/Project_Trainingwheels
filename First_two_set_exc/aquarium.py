lenght = int(input())
width = int(input())
height = int(input())
water_volume_occupied = float(input())

""" The variables go here  """
tank_volume = lenght*width*height
total_water = tank_volume*0.001
percent_water_volume_occupied = water_volume_occupied*0.01
water_needed = total_water*(1-percent_water_volume_occupied)

print(water_needed)
