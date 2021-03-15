line_of_path = input().split(f"{chr(92)}")
new_word = line_of_path[len(line_of_path)-1]
file_name, file_extension = new_word.split(".")

print(f"File name: {file_name}")
print(f"File extension: {file_extension}")
