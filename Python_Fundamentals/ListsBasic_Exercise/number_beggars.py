total_offers_string = input().split(", ")
total_beggars = int(input())


start_index_for_offers = 0
lst_total_offers = []

for beggar in range(1, total_beggars + 1):
    single_beggar_offer = 0
    for offer in range(start_index_for_offers, len(total_offers_string), total_beggars):
        single_beggar_offer += int(total_offers_string[offer])
    lst_total_offers.append(single_beggar_offer)
    start_index_for_offers += 1

print(lst_total_offers)



