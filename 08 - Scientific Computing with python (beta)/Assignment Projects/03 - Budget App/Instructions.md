
# Budget App

## Overview
Complete the `Category` class. This class is part of a budget application, where each instance represents a budget category such as food, clothing, and entertainment.

## Class Specifications

### Class: `Category`

- **Initialization**:
  - When objects are created, they are passed in the name of the category.
  - The class should have an instance variable called `ledger` that is a list.

- **Methods**:
  - `deposit(amount, description="")`: Appends an object to the ledger list in the form of `{"amount": amount, "description": description}`.
  - `withdraw(amount, description="")`: Similar to the deposit method, but stores the amount as a negative number in the ledger. Returns `True` if the withdrawal took place, and `False` otherwise.
  - `get_balance()`: Returns the current balance of the budget category based on the deposits and withdrawals that have occurred.
  - `transfer(amount, destination)`: Transfers an amount to another budget category. Adds a withdrawal to the current category's ledger and a deposit to the destination category's ledger with respective descriptions. Returns `True` if the transfer took place, and `False` otherwise.
  - `check_funds(amount)`: Returns `False` if the amount is greater than the balance of the budget category and `True` otherwise. This method should be used by both the withdraw method and transfer method.

- **String Representation**:
  - When the budget object is printed, it should display:
    - A title line of 30 characters where the name of the category is centered in a line of '*' characters.
    - A list of the items in the ledger. Each line should show the description and amount. The first 23 characters of the description should be displayed, then the amount. The amount should be right aligned, contain two decimal places, and display a maximum of 7 characters.
    - A line displaying the category total.

### Function: `create_spend_chart(categories)`
- Takes a list of category instances as an argument.
- Returns a string that is a bar chart representing the percentage spent in each category. 
- The percentage spent is calculated only with withdrawals.
- The chart features labels from 0 - 100 on the left, with each bar made from the "o" character, rounded down to the nearest 10.
- The category names should be written vertically below the bars.
- The title of the chart is "Percentage spent by category".

## Example Usage

```python
food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
clothing = Category("Clothing")
food.transfer(50, clothing)
print(food)
```

### Expected Output

```
*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96
```

This function will be tested with up to four categories. Pay close attention to the spacing and punctuation of the results.
