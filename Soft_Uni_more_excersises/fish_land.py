skumria_price = float(input())
tsatsa_price = float(input())
palamud_kg = float(input())
safrid_kg = float(input())
midi_kg = int(input())

palamud_price = skumria_price + (skumria_price * 0.60)
safrid_price = tsatsa_price + (tsatsa_price * 0.80)
midi_price = 7.5

total = ((palamud_kg * palamud_price) + (safrid_kg * safrid_price) + (midi_kg * midi_price))

print(f'{total:.2f}')