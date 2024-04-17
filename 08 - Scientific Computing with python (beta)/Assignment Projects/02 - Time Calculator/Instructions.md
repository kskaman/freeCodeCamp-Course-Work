
# Time Calculator

## Function Requirements

Write a function named `add_time` that takes in two required parameters and one optional parameter:
- **start time**: a start time in the 12-hour clock format (ending in AM or PM)
- **duration time**: a duration time that indicates the number of hours and minutes
- **starting day of the week (optional)**: case insensitive

## Function Behavior

The function should add the duration time to the start time and return the result.

- **Next Day**: If the result will be the next day, it should show "(next day)" after the time.
- **Multiple Days Later**: If the result will be more than one day later, it should show "(n days later)" after the time, where "n" is the number of days later.
- **Day of the Week**: If the function is given the optional starting day of the week parameter, then the output should display the day of the week of the result. The day of the week in the output should appear after the time and before the number of days later.

## Examples

Below are some examples of different cases the function should handle. Pay close attention to the spacing and punctuation of the results.

1. **Example 1**:
   ```python
   add_time('3:00 PM', '3:10')
   # Returns: 6:10 PM
   ```

2. **Example 2**:
   ```python
   add_time('11:30 AM', '2:32', 'Monday')
   # Returns: 2:02 PM, Monday
   ```

3. **Example 3**:
   ```python
   add_time('11:43 AM', '00:20')
   # Returns: 12:03 PM
   ```

4. **Example 4**:
   ```python
   add_time('10:10 PM', '3:30')
   # Returns: 1:40 AM (next day)
   ```

5. **Example 5**:
   ```python
   add_time('11:43 PM', '24:20', 'tueSday')
   # Returns: 12:03 AM, Thursday (2 days later)
   ```

6. **Example 6**:
   ```python
   add_time('6:30 PM', '205:12')
   # Returns: 7:42 AM (9 days later)
   ```

**Note**: Do not import any Python libraries. Assume that the start times are valid times. The minutes in the duration time will be a whole number less than 60, but the hour can be any whole number.
