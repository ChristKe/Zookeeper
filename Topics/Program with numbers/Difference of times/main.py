# put your python code here
hours = 3600
minutes = 60
run_hour = int(input()) * hours
run_minutes = int(input()) * minutes
run_sec = int(input())
rain_hour = int(input()) * hours
rain_minutes = int(input()) * minutes
rain_sec = int(input())
final_to_sec = ((rain_hour + rain_minutes + rain_sec) - (run_hour + run_minutes + run_sec))
print(final_to_sec)