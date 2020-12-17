volume = int(input())
water_flow1 = int(input())
water_flow2 = int(input())
hours_leave = float(input())

first_pipe_result = water_flow1 * hours_leave
second_pipe_result = water_flow2 * hours_leave
first_second_pipe_total = first_pipe_result + second_pipe_result
percent_from_volume = (first_second_pipe_total / volume) * 100
percent_from_volume1 = (first_pipe_result / first_second_pipe_total) * 100
percent_from_volume2 = (second_pipe_result / first_second_pipe_total) * 100
if volume >= first_second_pipe_total:
    print(f"The pool is {percent_from_volume:.2f}% full. Pipe 1: {percent_from_volume1:.2f}%. "
          f"Pipe 2: {percent_from_volume2:.2f}%.")
elif volume < first_second_pipe_total:
    print(f'For {hours_leave} hours the pool overflows  with {first_second_pipe_total - volume:.2f} liters.')