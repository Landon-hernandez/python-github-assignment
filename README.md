# Study Time Tracker

A tiny Python program that asks how many hours you study per day, estimates weekly study hours, and shows progress toward a weekly study goal.

## How to run

From the project folder run:

```bash
python app.py
# or, on some systems:
python3 app.py
```

## Example interaction

```
Welcome to my Python program!
How many hours did you study today? 2
What is your weekly study goal in hours? (press Enter to use 14) 

If you study 2.00 hours per day, you'll study about 14.00 hours this week.
That is 100.0% of your 14-hour weekly goal.
Great job — you're meeting or exceeding your weekly goal!
```

## Notes

- The program includes basic error handling for non-numeric input.
- Default weekly goal is 14 hours if you press Enter without entering a value.
