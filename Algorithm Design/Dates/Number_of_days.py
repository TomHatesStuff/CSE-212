def is_leap_year(year):
    # Check if a given year is a leap year.
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)

def validate_date(year, month, day):
    # Validate the input date.
    assert year >= 1753, "Year must be 1753 or later"
    assert 1 <= month <= 12, "Month must be between 1 and 12"
    assert 1 <= day <= 31, "Day must be between 1 and 31"
    assert not (day == 31 and (month == 4 or month == 6 or month == 9 or month == 11)), f"Invalid day ({day}) for month {month}"
    if month == 2:
        assert not (day > 29 or (day == 29 and not is_leap_year(year))), f"Invalid day ({day}) for February {year}"
    return True

def get_date(prompt):
    # Prompt the user for a date.
    while True:
        try:
            year = int(input(prompt + " year: "))
            month = int(input(prompt + " month: "))
            day = int(input(prompt + " day: "))
            if validate_date(year, month, day):
                return year, month, day
            else:
                print("Invalid date. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

def days_between_dates(start_year, start_month, start_day, end_year, end_month, end_day):
    # Compute the number of days between two dates.
    assert (start_year, start_month, start_day) <= (end_year, end_month, end_day), "Start date cannot be later than end date"

    days_in_month = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    days = 0
    while (start_year, start_month, start_day) != (end_year, end_month, end_day):
        days += 1
        start_day += 1
        if start_day > days_in_month[start_month]:
            start_day = 1
            start_month += 1
            if start_month > 12:
                start_month = 1
                start_year += 1
                if is_leap_year(start_year):
                    days_in_month[2] = 29
                else:
                    days_in_month[2] = 28
    return days

# Input dates from the user
start_year, start_month, start_day = get_date("Start")
end_year, end_month, end_day = get_date("End")

# Compute and print the number of days between the two dates
days = days_between_dates(start_year, start_month, start_day, end_year, end_month, end_day)
if days == 0:
    print("Error: Start date is later than end date.")
else:
    print(f"There are {days} days")
# 1. Name:
#      Luke Marshall
# 2. Assignment Name:
#      Lab 10: Number of Days
# 3. Assignment Description:
#      Takes two dates and computes how many days is between them and includes leap years.
# 4. What was the hardest part? Be as specific as possible.
#      THe hardest part was that i forgot to include the if end date is before start date. And then my code got screwed up. I also had issues making the video.
# 5. How long did it take for you to complete the assignment?
#      12 hours