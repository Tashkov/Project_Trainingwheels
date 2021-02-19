line = int(input())

def loading_bar(number):
    amount = number // 10
    loading_element = "%"
    filling_bar = "."
    bar = f"{line}% [{loading_element * amount}{filling_bar * (10 - amount)}]"
    if amount < 10:
        message = f"\nStill loading..."
        bar += message
        return bar
    else:
        message = f"{line}% Complete!\n"
        message += f"[{loading_element * amount}{filling_bar * (10 - amount)}]"
        return message





print(loading_bar(line))