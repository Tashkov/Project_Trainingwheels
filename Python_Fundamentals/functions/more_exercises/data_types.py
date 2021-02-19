def data_type_reader(type, value):
    if type == 'int':
        return int(value) * 2
    if type == 'real':
        return f"{float(value) * 1.5:.2f}"
    if type == "string":
        return f"${value}$"

type = input()
value = input()

print(data_type_reader(type, value))