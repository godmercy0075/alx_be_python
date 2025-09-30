# daily_reminder.py

# Prompt for a single task
task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ").lower()
time_bound = input("Is it time-bound? (yes/no): ").lower()

# Process the task using match-case
match priority:
    case "high":
        message = f"Reminder: '{task}' is a high priority task."
    case "medium":
        message = f"Reminder: '{task}' is a medium priority task."
    case "low":
        message = f"Note: '{task}' is a low priority task."
    case _:
        message = f"'{task}' has an unknown priority level."

# Modify message if time-bound
if time_bound == "yes":
    message += " It requires immediate attention today!"
else:
    message += " Consider completing it when you have free time."

# Print customized reminder
print(message)
