journal = input().split(', ')
line = input()

while line != "Craft!":
    list_items = line.split(" - ")
    command = list_items[0]
    item = list_items[1]

    if command == "Collect":
        if item not in journal:
            journal.append(item)
    if command == "Drop":
        if item in journal:
            journal.remove(item)
    if command == "Combine Items":
        new_list = item.split(":")
        old_item = new_list[0]
        new_item = new_list[1]
        if old_item in journal:
            index_old_item = journal.index(old_item)
            if index_old_item == len(journal):
                journal.append(new_item)
            else:
                journal.insert(index_old_item + 1, new_item)
    if command == "Renew":
        if item in journal:
            journal.remove(item)
            journal.append(item)

    line = input()

print(*journal, sep=", ")
