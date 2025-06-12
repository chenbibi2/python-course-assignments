from datetime import datetime, timedelta

raw_schedule = """
09:20 Introduction
11:00 Exercises
11:15 Break
11:35 Numbers and strings
12:30 Lunch Break
13:30 Exercises
14:10 Solutions
14:30 Break
14:40 Lists
15:40 Exercises
17:00 Solutions
17:30 End

09:30 Lists and Tuples
10:30 Break
10:50 Exercises
12:00 Solutions
12:30 Dictionaries
12:45 Lunch Break
14:15 Exercises
16:00 Solutions
16:15 Break
16:30 Functions
17:00 Exercises
17:30 End
"""

sessions = raw_schedule.strip().split("\n\n")
parsed_schedules = []

for session in sessions:
    lines = session.split("\n")
    parsed_schedule = []
    for i in range(len(lines) - 1):
        start_time = lines[i].split(" ")[0]
        end_time = lines[i + 1].split(" ")[0]
        activity = " ".join(lines[i].split(" ")[1:])
        parsed_schedule.append((start_time, end_time, activity))
    parsed_schedules.append(parsed_schedule)

formatted_schedule = []
durations = {}

for schedule in parsed_schedules:
    for start_time, end_time, activity in schedule:
        formatted_schedule.append(f"{start_time}-{end_time} {activity}")
        start_dt = datetime.strptime(start_time, "%H:%M")
        end_dt = datetime.strptime(end_time, "%H:%M")
        duration = int((end_dt - start_dt).total_seconds() / 60)
        if activity != "End":
            durations[activity] = durations.get(activity, 0) + duration

total_time = sum(durations.values())
summary = [
    f"{activity:<25} {duration:>4} minutes   {duration / total_time * 100:>2.0f}%"
    for activity, duration in sorted(durations.items())
]

print("\n".join(formatted_schedule))
print("\n" + "\n".join(summary))
