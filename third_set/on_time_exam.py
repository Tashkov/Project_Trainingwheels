start_h = int(input())
start_m = int(input())
arrival_h = int(input())
arrival_m = int(input())

"""Format the input into minutes and store it into new variables later on
later on do the calculations """
"""On time"""
if start_h == arrival_h and start_m == arrival_m:
    print("One time")
elif start_h - arrival_h == 1 and 60 - arrival_m <= 30:
    print(f"On time\n{60 - arrival_m:02d} minutes on time")

"""Late"""
if start_h != arrival_h and start_m != arrival_m or start_h == arrival_h and start_m != arrival_m:
    if start_h == arrival_h and start_m != arrival_m:
        if arrival_m > start_m:
            print(f"Late\n{arrival_m - start_m} minutes after the start")
    elif start_h > arrival_h and start_m == arrival_m:
        print(f"Late\n{start_h - arrival_h}:{arrival_m:02d} hours after the start")
    elif start_h > arrival_h and start_m < arrival_m:
        print(f"Late\n{start_h - arrival_h}:{start_m - arrival_m:02d} hours after the start")



"""    
elif start_h > arrival_h and arrival_m - start_m >= 30:
    print(f"On time\n{60 - arrival_m:02d} minutes before the start")

if start_h > arrival_h and start_m > arrival_m:
    print(f"Late\n{arrival_h - start_h}:{arrival_m - start_m:02d} hours after the start")

if start_h > arrival_h and start_m == arrival_m:
    print(f"Early\n{start_h - arrival_h}:{arrival_m:02d} hours before the start")

if start_h == arrival_h and start_m != arrival_m:
    if arrival_m > start_m:
        print(f"Late\n{arrival_m - start_m} minutes after the start")
    elif start_m < (arrival_m + 60):
        print(f"Late\n{(arrival_m + 60) - start_m} minutes late")
    elif arrival_m < start_m:
        print(f"Early\n{start_m - arrival_m} minutes before the start")
    elif arrival_m < (start_m+60):
        print(f"Early\n{(start_m-60) - arrival_m} minutes before the start")
elif start_h != arrival_h and start_m != arrival_m:
    if start_h > arrival_h and start_m > arrival_m:
        print(f"Late\n{arrival_h - start_h}:{arrival_m - start_m:02d} hours after the start")

    

elif start_h == arrival_h and start_m < arrival_m:
    if arrival_m < start_m:
        print(f"Early\n{start_m - arrival_m} minutes before the start")
    elif arrival_m < (start_m+60):
        print(f"Early\n{(start_m-60) - arrival_m} minutes before the start")
"""
"""Fix the remaining issues and test out beforehand
"""