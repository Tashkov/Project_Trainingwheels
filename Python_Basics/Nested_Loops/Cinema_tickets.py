line = input()
total_tickets = 0
standard_tickets = 0
student_tickets = 0
kid_tickets = 0

while line != "Finish":
    movie_name = line
    free_seats = int(input())
    sold_tickets_per_movie = 0

    command = input()
    while command != "End":
        ticket_type = command
        total_tickets += 1
        sold_tickets_per_movie += 1

        if ticket_type == "standard":
            standard_tickets += 1
        elif ticket_type == "student":
            student_tickets += 1
        elif ticket_type == "kid":
            kid_tickets += 1
        if sold_tickets_per_movie == free_seats:
            break
        command = input()

    percent_theater_seats = sold_tickets_per_movie / free_seats * 100
    print(f"{movie_name} - {percent_theater_seats:.2f}% full.")
    line = input()

print(f"Total tickets: {total_tickets}")
print(f"{(student_tickets / total_tickets) * 100:.2f}% student tickets.")
print(f"{(standard_tickets / total_tickets) * 100:.2f}% standard tickets.")
print(f"{(kid_tickets / total_tickets) * 100:.2f}% kids tickets.")