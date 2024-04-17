def add_time(start, duration, weekday=None):
    
    # Splitting start time into components
    start_parts = start.split()
    time_part = start_parts[0].split(':')
    am_pm = start_parts[1]
    
    # Extracting start hours and minutes
    start_hours = int(time_part[0])
    start_minutes = int(time_part[1])
    
    # Splitting duration into hours and minutes
    duration_parts = duration.split(':')
    duration_hours = int(duration_parts[0])
    duration_minutes = int(duration_parts[1])
    
    # Calculate the new minutes and hours
    new_minutes = start_minutes + duration_minutes
    # Additional hours from minutes overflow
    additional_hours = new_minutes // 60  
    new_minutes %= 60
    new_hours = start_hours + duration_hours + additional_hours
    
    # Handling AM/PM and calculating the number of days passed
    # Every 12 hours, AM/PM changes
    periods = new_hours // 12  
    am_pm_change = (periods % 2 == 1)
    if am_pm == "PM" and am_pm_change:
        days_later = 1 + (periods // 2)
    else:
        days_later = periods // 2
    
    new_hours %= 12
    # Handling the 0 hour case to 12 hour format
    new_hours = 12 if new_hours == 0 else new_hours  
    am_pm = "PM" if (periods + (1 if am_pm == "PM" else 0)) % 2 != 0 else "AM"
    
    # Format new time
    new_time = f"{new_hours}:{new_minutes:02} {am_pm}"
    
    # Handling weekday
    if weekday:
        days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        current_day_index = days_of_week.index(weekday.capitalize())
        new_day_index = (current_day_index + days_later) % 7
        new_day = days_of_week[new_day_index]
        new_time += f", {new_day}"
    
    # Adding information about the number of days later
    if days_later == 1:
        new_time += " (next day)"
    elif days_later > 1:
        new_time += f" ({days_later} days later)"
    
    return new_time

# Test examples
print(add_time('3:00 PM', '3:10'))  # Returns: 6:10 PM
print(add_time('11:30 AM', '2:32', 'Monday'))  # Returns: 2:02 PM, Monday
print(add_time('11:43 AM', '00:20'))  # Returns: 12:03 PM
print(add_time('10:10 PM', '3:30'))  # Returns: 1:40 AM (next day)
print(add_time('11:43 PM', '24:20', 'tueSday'))  # Returns: 12:03 AM, Thursday (2 days later)
print(add_time('6:30 PM', '205:12'))  # Returns: 7:42 AM (9 days later)
