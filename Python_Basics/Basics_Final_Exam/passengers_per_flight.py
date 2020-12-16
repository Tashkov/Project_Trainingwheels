from math import floor

companies_count = int(input())
base_median = 0
company_name_most_flights = ""

for i in range(companies_count):
    company_name = input()
    passengers_number = input()
    passengers_total = 0
    flights_counter = 0
    while passengers_number != "Finish":
        passengers_total += int(passengers_number)
        flights_counter += 1
        passengers_median = floor(passengers_total / flights_counter)
        passengers_number = input()
    if base_median <= passengers_median:
        base_median = passengers_median
        company_name_most_flights = company_name

    print(f"{company_name}: {passengers_median} passengers.")

print(f"{company_name_most_flights} has most passengers per flight: {base_median}")


