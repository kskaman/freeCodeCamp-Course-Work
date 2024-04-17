
# Budget App Tests

## Test Cases

Here are the provided test cases for the `Category` class methods and `create_spend_chart` function:

1. **Deposit Method Tests**:
   - The deposit method should create a specific object in the ledger instance variable.
   - Calling the deposit method with no description should create a blank description.

2. **Withdraw Method Tests**:
   - The withdraw method should create a specific object in the ledger instance variable.
   - Calling the withdraw method with no description should create a blank description.
   - The withdraw method should return True if the withdrawal took place.
   - Calling `food.deposit(900, "deposit")` and `food.withdraw(45.67, "milk, cereal, eggs, bacon, bread")` should return a balance of 854.33.
   - The withdraw method should return False if the withdrawal didn't take place.

3. **Transfer Method Tests**:
   - Calling the transfer method on a category object should create a specific ledger item in that category object.
   - The transfer method should return True if the transfer took place.
   - Calling transfer on a category object should reduce the balance in the category object.
   - The transfer method should increase the balance of the category object passed as its argument.
   - The transfer method should create a specific ledger item in the category object passed as its argument.
   - The transfer method should return False if the transfer didn't take place.

4. **Check Funds Method Tests**:
   - The check_funds method should return False if the amount passed to the method is greater than the category balance.
   - The check_funds method should return True if the amount passed to the method is not greater than the category balance.

5. **Printing Category Instance**:
   - Printing a Category instance should give a different string representation of the object.

6. **Create Spend Chart Function**:
   - `create_spend_chart` should print a different chart representation. Check that all spacing is exact.
