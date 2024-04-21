
# Polygon Area Calculator

## Overview
This project involves using object-oriented programming to create a `Rectangle` class and a `Square` class. The `Square` class should be a subclass of `Rectangle`, inheriting its methods and attributes.

## Class Definitions

### Class: `Rectangle`
- **Attributes**:
  - `width`: the width of the rectangle
  - `height`: the height of the rectangle

- **Methods**:
  - `set_width(self, width)`: Sets the width of the rectangle.
  - `set_height(self, height)`: Sets the height of the rectangle.
  - `get_area(self)`: Returns the area of the rectangle (`width * height`).
  - `get_perimeter(self)`: Returns the perimeter (`2 * width + 2 * height`).
  - `get_diagonal(self)`: Returns the diagonal length (`(width ** 2 + height ** 2) ** .5`).
  - `get_picture(self)`: Returns a string that represents the rectangle with lines of "*" where each line's length is equal to the width and the number of lines is equal to the height. If width or height is larger than 50, returns "Too big for picture."
  - `get_amount_inside(self, shape)`: Takes another shape (either another rectangle or a square) and returns the number of times the passed shape can fit inside the rectangle without rotation.
  
- **String Representation**:
  - When a `Rectangle` instance is printed, it should display in the format: `Rectangle(width=X, height=Y)`

### Class: `Square` (subclass of `Rectangle`)
- **Initialization**:
  - Accepts a single argument for side length, setting both width and height to this value.
  
- **Methods**:
  - `set_side(self, side)`: Sets both the width and height to the given side length.
  - Inherits all methods from `Rectangle` but ensures that any changes to width or height apply to both due to the nature of a square.
  - Additionally, the set_width and set_height methods on the Square class should set both the width and height.
  
- **String Representation**:
  - When a `Square` instance is printed, it should display in the format: `Square(side=X)`

## Usage Example
```python
rect = Rectangle(10, 5)
print(rect.get_area())  # Outputs: 50
rect.set_height(3)
print(rect.get_perimeter())  # Outputs: 26
print(rect)  # Outputs: Rectangle(width=10, height=3)
print(rect.get_picture())  # Outputs the picture representation

sq = Square(9)
print(sq.get_area())  # Outputs: 81
sq.set_side(4)
print(sq.get_diagonal())  # Outputs: 5.656854249492381
print(sq)  # Outputs: Square(side=4)
print(sq.get_picture())  # Outputs the picture representation

rect.set_height(8)
rect.set_width(16)
print(rect.get_amount_inside(sq))  # Outputs: 8
```
