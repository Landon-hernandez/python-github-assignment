#!/usr/bin/env python3
# app.py
#!/usr/bin/env python3
# app.py
#!/usr/bin/env python3
# app.py
# Study Time Tracker
# Asks for daily study hours, estimates weekly hours, compares to a weekly goal,
# and handles basic input errors.

def main():
    print("Welcome to my Python program!")

    # Ask the user for input (daily hours)
    daily_input = input("How many hours did you study today? ")

    # Basic error handling for non-numeric input
    try:
        daily_hours = float(daily_input)
    except ValueError:
        print("Please enter a valid number for hours (e.g. 2 or 1.5).")
        return

    # Estimate weekly hours from daily hours
    weekly_hours = daily_hours * 7

    # Optional: ask for a weekly goal (with a sensible default)
    goal_input = input("What is your weekly study goal in hours? (press Enter to use 14) ")
    try:
        if goal_input.strip() == "":
            weekly_goal = 14.0
        else:
            weekly_goal = float(goal_input)
    except ValueError:
        print("Invalid number for goal. Using default weekly goal = 14 hours.")
        weekly_goal = 14.0

    # Avoid division by zero
    if weekly_goal == 0:
        percent_of_goal = 0.0
    else:
        percent_of_goal = (weekly_hours / weekly_goal) * 100

    # Clear formatted output
    print()
    print(f"If you study {daily_hours:.2f} hours per day, you'll study about {weekly_hours:.2f} hours this week.")
    print(f"That is {percent_of_goal:.1f}% of your {weekly_goal:.0f}-hour weekly goal.")
    if percent_of_goal >= 100:
        print("Great job — you're meeting or exceeding your weekly goal!")
    else:
        remaining = max(0.0, weekly_goal - weekly_hours)
        print(f"You need about {remaining:.2f} more hours this week to reach the goal.")
    print()


if __name__ == "__main__":
    main()
