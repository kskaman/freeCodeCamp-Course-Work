
# Time Calculator Tests

## Test Cases

Here are the test cases for the `add_time` function and their expected outcomes:

1. **Test 1**:
   ```python
   add_time('3:30 PM', '2:12')
   # Should return: '5:42 PM'
   ```

2. **Test 2**:
   ```python
   add_time('11:55 AM', '3:12')
   # Should return: '3:07 PM'
   ```

3. **Expectation**:
   - Expected time to end with '(next day)' when it is the next day.
   - Expected period to change from AM to PM at 12:00.

4. **Test 3**:
   ```python
   add_time('2:59 AM', '24:00')
   # Should return: '2:59 AM (next day)'
   ```

5. **Test 4**:
   ```python
   add_time('11:59 PM', '24:05')
   # Should return: '12:04 AM (2 days later)'
   ```

6. **Test 5**:
   ```python
   add_time('8:16 PM', '466:02')
   # Should return: '6:18 AM (20 days later)'
   ```

7. **Expectation**:
   - Expected adding 0:00 to return the initial time.

8. **Test 6**:
   ```python
   add_time('3:30 PM', '2:12', 'Monday')
   # Should return: '5:42 PM, Monday'
   ```

9. **Test 7**:
   ```python
   add_time('2:59 AM', '24:00', 'saturDay')
   # Should return: '2:59 AM, Sunday (next day)'
   ```

10. **Test 8**:
    ```python
    add_time('11:59 PM', '24:05', 'Wednesday')
    # Should return: '12:04 AM, Friday (2 days later)'
    ```

11. **Test 9**:
    ```python
    add_time('8:16 PM', '466:02', 'tuesday')
    # Should return: '6:18 AM, Monday (20 days later)'
    ```