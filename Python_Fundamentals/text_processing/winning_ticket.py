tickets = input().split(", ")

for ticket in tickets:
    counter = 0
    if len(ticket) != 20:
        print("invalid ticket")
        break
    for index in range(0, 11):
        while not ticket[index].isalnum():
            while index + 1 <= 10:
                if ticket[index] == ticket[index+1] == "@":
                    counter += 1
                elif ticket[index] == ticket[index+1] == "#":
                    counter += 1
                elif ticket[index]== ticket[index+1] == "$":
                    counter += 1
                elif ticket[index]== ticket[index+1] == "^":
                    counter += 1
                index += 1
    for index in range(-1, -11, -1):
        while not ticket[index].isalnum():
            while index - 1 > -10:
                if ticket[index] == ticket[index-1] == "@":
                    counter += 1
                elif ticket[index] == ticket[index-1] == "#":
                    counter += 1
                elif ticket[index] == ticket[index-1] == "$":
                    counter += 1
                elif ticket[index] == ticket[index-1] == "^":
                    counter += 1
                index -= 1
