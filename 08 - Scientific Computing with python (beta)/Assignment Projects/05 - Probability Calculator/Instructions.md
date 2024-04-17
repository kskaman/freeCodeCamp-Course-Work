
# Probability Calculator

## Project Overview

In this project, you will write a program to determine the approximate probability of drawing certain balls randomly from a hat. This problem can be approached by simulating a large number of experiments.

## Class: `Hat`

- **Initialization**:
  - The `Hat` class should take a variable number of arguments that specify the number of balls of each color in the hat.
  - Examples of creating `Hat` objects:
    ```python
    hat1 = Hat(yellow=3, blue=2, green=6)
    hat2 = Hat(red=5, orange=4)
    hat3 = Hat(red=5, orange=4, black=1, blue=0, pink=2, striped=9)
    ```
  - The arguments passed to the `Hat` object should be converted into a `contents` instance variable. `contents` should be a list of strings, each representing a single ball of that color.

- **Methods**:
  - `draw(number_of_balls)`: This method should remove balls at random from `contents` and return those balls as a list of strings. If the number of balls to draw exceeds the available quantity, return all the balls.

## Function: `experiment`

- **Parameters**:
  - `hat`: A hat object.
  - `expected_balls`: An object indicating the exact group of balls to attempt to draw from the hat. For example, `{"blue":2, "red":1}`.
  - `num_balls_drawn`: The number of balls to draw out of the hat in each experiment.
  - `num_experiments`: The number of experiments to perform.

- **Behavior**:
  - The function should perform a specified number of experiments to determine the probability of drawing an expected group of balls from the hat.
  - For example:
    ```python
    hat = Hat(black=6, red=4, green=3)
    probability = experiment(hat=hat, expected_balls={"red":2, "green":1}, num_balls_drawn=5, num_experiments=2000)
    ```

- **Output**:
  - The function returns a probability based on the outcome of the experiments. Due to the randomness, the result may vary slightly with each run.

## Example Output

```python
>>> 0.356
```

**Hint**: You may consider using the modules that are already imported at the top. Do not initialize random seed within the file.
