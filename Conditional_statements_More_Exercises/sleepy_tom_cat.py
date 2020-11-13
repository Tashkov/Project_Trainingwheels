free_days = int(input())
tom_rest_default = 30000
work_days_total = 365 - free_days
play_time_total = (work_days_total * 63) + (free_days * 127)
hours = 0
minutes = 0

if play_time_total > tom_rest_default:
    minutes_more = play_time_total - tom_rest_default
    hours = minutes_more // 60
    minutes = minutes_more % 60
    print(f'Tom will run away\n{hours} hours and {minutes} minutes more for play')
elif play_time_total <= tom_rest_default:
    minutes_more = tom_rest_default - play_time_total
    hours = minutes_more // 60
    minutes = minutes_more % 60
    print(f'Tom sleeps well\n{hours} hours and {minutes} minutes less for play')
