pages_per_book = int(input())
pages_per_hour = int(input())
days_per_book = int(input())
total_time_book = pages_per_book / pages_per_hour

hours_per_day = total_time_book / days_per_book

print(hours_per_day)