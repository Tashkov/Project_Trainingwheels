line = input()
legendary_dict = {"shards": 0, "fragments": 0, "motes": 0}
junk_dict = {}

while True:
    token = line.split()
    weapon = ""
    loop_break = False
    for i in range(0, len(token), 2):
        quantity = int(token[i])
        material = token[i + 1].lower()
        if material in legendary_dict:
            legendary_dict[material] += quantity
            if legendary_dict.get(material) >= 250:
                if material == "shards":
                    weapon = "Shadowmourne"
                elif material == "fragments":
                    weapon = "Valanyr"
                elif material == "motes":
                    weapon = "Dragonwrath"
                legendary_dict[material] -= 250
                loop_break = True
                break
        else:
            if material not in junk_dict:
                junk_dict[material] = quantity
            else:
                junk_dict[material] += quantity
    if loop_break:
        break
    elif not loop_break:
        line = input()

sorted_legendary = dict(sorted(legendary_dict.items(), key=lambda kvp: (-kvp[1], kvp[0])))
sorted_junk = dict(sorted(junk_dict.items(), key=lambda kvp: kvp[0]))

print(f"{weapon} obtained!")
for key, value in sorted_legendary.items():
    print(f"{key}: {value}")
for key2, value2 in sorted_junk.items():
    print(f"{key2}: {value2}")
