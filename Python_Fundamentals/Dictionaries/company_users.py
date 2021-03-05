line = input()
company_DB = {}

while not line == "End":
    token = line.split(" -> ")
    name = token[0]
    number = token[1]
    if name not in company_DB:
        company_DB[name] = []
        if number not in company_DB[name]:
            company_DB[name].append(number)
    else:
        if number not in company_DB[name]:
            company_DB[name].append(number)

    line = input()
sorted_company_DB = dict(sorted(company_DB.items()))

for key, value in sorted_company_DB.items():
    print(key)
    sorted(value)
    for id_number in value:
        print(f"-- {id_number}")