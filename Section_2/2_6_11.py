hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
min_total = mins + dura

if min_total > 60:
    mins = min_total % 60

    hour += min_total // 60
    if hour > 24 or hour < 0:
        hour = hour % 24
else:
    mins = min_total
print(hour,":",mins)