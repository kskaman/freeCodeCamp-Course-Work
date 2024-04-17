
# Arithmetic Formatter Tests

Here are the provided test cases and their expected results for the `arithmetic_arranger` function:

1. Test:
   ```python
   arithmetic_arranger(["3801 - 2", "123 + 49"])
   ```
   Expected Output:
   ```
   3801      123
   -    2    +  49
   ------    -----
   ```

2. Test:
   ```python
   arithmetic_arranger(["1 + 2", "1 - 9380"])
   ```
   Expected Output:
   ```
   1         1
   + 2    - 9380
   ---    ------
   ```

3. Test:
   ```python
   arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"])
   ```
   Expected Output:
   ```
     3      3801      45      123
   + 855    -    2    + 43    +  49
   -----    ------    ----    -----
   ```

4. Test:
   ```python
   arithmetic_arranger(["11 + 4", "3801 - 2999", "1 + 2", "123 + 49", "1 - 9380"])
   ```
   Expected Output:
   ```
   11      3801      1      123         1
   +  4    - 2999    + 2    +  49    - 9380
   ----    ------    ---    -----    ------
   ```

5. Test:
   ```python
   arithmetic_arranger(["44 + 815", "909 - 2", "45 + 43", "123 + 49", "888 + 40", "653 + 87"])
   ```
   Expected Output:
   ```
   'Error: Too many problems.'
   ```

6. Test:
   ```python
   arithmetic_arranger(["3 / 855", "3801 - 2", "45 + 43", "123 + 49"])
   ```
   Expected Output:
   ```
   "Error: Operator must be '+' or '-'."
   ```

7. Test:
   ```python
   arithmetic_arranger(["24 + 85215", "3801 - 2", "45 + 43", "123 + 49"])
   ```
   Expected Output:
   ```
   'Error: Numbers cannot be more than four digits.'
   ```

8. Test:
   ```python
   arithmetic_arranger(["98 + 3g5", "3801 - 2", "45 + 43", "123 + 49"])
   ```
   Expected Output:
   ```
   'Error: Numbers must only contain digits.'
   ```

9. Test:
   ```python
   arithmetic_arranger(["3 + 855", "988 + 40"], True)
   ```
   Expected Output:
   ```
     3      988
   + 855    +  40
   -----    -----
     858     1028
   ```

10. Test:
    ```python
    arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True)
    ```
    Expected Output:
    ```
       32         1      45      123      988
   - 698    - 3801    + 43    +  49    +  40
   -----    ------    ----    -----    -----
    -666     -3800      88      172     1028
    ```
