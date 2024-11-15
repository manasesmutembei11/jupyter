def add_time(start, duration, starting_day=None):
    # Days of the week for indexing
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

    # Step 1: Parse the start time
    start_time, meridian = start.split()
    start_hour, start_minute = map(int, start_time.split(":"))

    # Convert to 24-hour format for easier calculation
    if meridian == "PM" and start_hour != 12:
        start_hour += 12
    if meridian == "AM" and start_hour == 12:
        start_hour = 0

    # Step 2: Parse the duration time
    duration_hour, duration_minute = map(int, duration.split(":"))

    # Step 3: Add the minutes and handle overflow to hours
    new_minute = start_minute + duration_minute
    extra_hour = new_minute // 60
    new_minute %= 60

    # Step 4: Add the hours, calculate total days passed
    new_hour = start_hour + duration_hour + extra_hour
    days_passed = new_hour // 24
    new_hour %= 24

    # Step 5: Determine new AM/PM and adjust hour back to 12-hour format
    if new_hour >= 12:
        new_meridian = "PM"
    else:
        new_meridian = "AM"

    if new_hour == 0:
        final_hour = 12
    else:
        final_hour = new_hour if new_hour <= 12 else new_hour - 12

    # Step 6: Adjust day of the week if provided
    if starting_day:
        start_day_index = days_of_week.index(starting_day.capitalize())
        new_day_index = (start_day_index + days_passed) % 7
        new_day = days_of_week[new_day_index]
        day_str = f", {new_day}"
    else:
        day_str = ""

    # Step 7: Add suffix for days passed
    if days_passed == 1:
        days_str = " (next day)"
    elif days_passed > 1:
        days_str = f" ({days_passed} days later)"
    else:
        days_str = ""

    # Step 8: Format and return the result
    new_time = f"{final_hour}:{new_minute:02} {new_meridian}{day_str}{days_str}"
    return new_time