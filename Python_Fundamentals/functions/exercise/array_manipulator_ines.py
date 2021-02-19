def exchange(nums_list, index):
    if len(nums_list) < index:
        return "Invalid index"
    else:
        first_part = nums_list[index+1:]
        second_part = nums_list[:index+1]
        result = first_part + second_part
        return result

def find_max_num(nums, odd_or_even):
    filtered_nums = []
    count = 0
    if odd_or_even == "odd":
        filtered_nums = [el for el in nums if not el % 2 == 0]
    else:
        filtered_nums = [el for el in nums if el % 2 == 0]
    if not filtered_nums:
        return "No matches"
    max_element = max(filtered_nums)
    for element in nums:
        if max_element == element:
            count += 1
    if count > 2:
        index = len(nums) - nums[::-1].index(max_element) - 1
    else:
        index = nums.index(max_element)
    return index

def find_min_num(nums_list, odd_or_even):
    filtered_nums = []
    count = 0
    if odd_or_even == "odd":
        filtered_nums = [el for el in nums if not el % 2 == 0]
    else:
        filtered_nums = [el for el in nums if el % 2 == 0]

    if not filtered_nums:
        return "No matches"
    min_element = min(filtered_nums)
    for element in nums:
        if min_element == element:
            count += 1
    if count > 2:
        index = len(nums) - nums[::-1].index(min_element) - 1
    else:
        index = nums.index(min_element)
    return index

def find_first(nums_list, count, odd_or_even):
    filtered_nums = []
    if odd_or_even == "odd":
        filtered_nums = [el for el in nums if not el % 2 == 0]
    else:
        filtered_nums = [el for el in nums if el % 2 == 0]
    if len(nums_list) < count:
        return "Invalid count"
    return filtered_nums[:count]

def find_last(nums_list, count, odd_or_even):
    filtered_nums = []
    if odd_or_even == "odd":
        filtered_nums = [el for el in nums if not el % 2 == 0]
    else:
        filtered_nums = [el for el in nums if el % 2 == 0]
    if len(nums_list) < count:
        return "Invalid count"
    return filtered_nums[-1:-count:-1]


nums = list(map(lambda x: int(x), input().split()))
command_data = input()

while not command_data == "end":
    command_data = command_data.split()
    command = command_data[0]
    if command == "exchange":
        i = int(command_data[1])
        result = exchange(nums, i)
        if result == "Invalid index":
            print(result)
        else:
            nums = exchange(nums, i)
    elif command == "max":
        odd_or_even = command_data[1]
        print(find_max_num(nums, odd_or_even))
    elif command == "min":
        odd_or_even = command_data[1]
        print(find_min_num(nums, odd_or_even))
    elif command == "first":
        count = int(command_data[1])
        odd_or_even = command_data[2]
        print(find_first(nums, count, odd_or_even))
    elif command == "last":
        count = int(command_data[1])
        odd_or_even = command_data[2]
        print(find_last(nums,count, odd_or_even))

    command_data = input()

if command_data == "end":
    print(nums)
