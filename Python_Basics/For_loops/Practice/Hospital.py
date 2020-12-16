time_frame = int(input())
doctors = 7
treated_patients = 0
untreated_patients = 0

for i in range(1, time_frame + 1):
    number = int(input())
    if i % 3 == 0 and untreated_patients > treated_patients:
        doctors += 1
    if number > doctors:
        untreated_patients += number - doctors
        treated_patients += abs(number - (number - doctors))
    elif number <= doctors:
        treated_patients += number

print(f'Treated patients: {treated_patients}.\nUntreated patients: {untreated_patients}.')