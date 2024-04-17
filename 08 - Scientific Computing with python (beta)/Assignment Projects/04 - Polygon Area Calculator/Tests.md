
# Polygon Area Calculator Tests

## Test Cases

Here are the provided test cases for the `Rectangle` and `Square` classes:

1. **Class Hierarchy**:
   - The Square class should be a subclass of the Rectangle class.
   - The Square class should be a distinct class from the Rectangle class.
   - A square object should be an instance of both the Square class and the Rectangle class.
   Status: Waiting

2. **String Representations**:
   - `Rectangle(3, 6)` should be represented as `Rectangle(width=3, height=6)`.
   - `Square(5)` should be represented as `Square(side=5)`.
   - Instances should reflect new string representations after setting new values.
   Status: Waiting

3. **Area Calculations**:
   - `Rectangle(3, 6).get_area()` should return 18.
   - `Square(5).get_area()` should return 25.
   Status: Waiting

4. **Perimeter Calculations**:
   - `Rectangle(3, 6).get_perimeter()` should return 18.
   - `Square(5).get_perimeter()` should return 20.
   Status: Waiting

5. **Diagonal Calculations**:
   - `Rectangle(3, 6).get_diagonal()` should return approximately 6.708203932499369.
   - `Square(5).get_diagonal()` should return approximately 7.0710678118654755.
   Status: Waiting

6. **Picture Method**:
   - The `.get_picture()` method should return a correct string representation for Rectangle and Square instances.
   - If the width or height is larger than 50, it should return "Too big for picture."
   Status: Waiting

7. **Amount Inside**:
   - `Rectangle(15,10).get_amount_inside(Square(5))` should return 6.
   - `Rectangle(4,8).get_amount_inside(Rectangle(3, 6))` should return 1.
   - `Rectangle(2,3).get_amount_inside(Rectangle(3, 6))` should return 0.
   Status: Waiting
