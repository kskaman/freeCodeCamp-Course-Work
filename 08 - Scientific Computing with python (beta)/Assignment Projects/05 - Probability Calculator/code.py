import copy
import random

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for ball, count in balls.items():
            self.contents.extend([ball]*count)
            print(self.contents)
        
    def draw(self, number):
        number = min(number, len(self.contents))
        drawn_balls = random.sample(self.contents, number)
        for ball in drawn_balls:
            self.contents.remove(ball)
        return drawn_balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    M = 0
    for _ in range(num_experiments):
        test_hat = copy.deepcopy(hat)
        drawn_balls = test_hat.draw(num_balls_drawn)
        success = True
        drawn_balls_count = {}
        for ball in drawn_balls:
            if ball in drawn_balls_count:
                drawn_balls_count[ball] += 1
            else:
                drawn_balls_count[ball] = 1
        
        for ball, count in expected_balls.items():
            if drawn_balls_count.get(ball, 0) < count:
                success = False
                break
        
        if success:
            M += 1

    return M / num_experiments


# Example usage:
hat = Hat(blue=5, red=4, green=2)
probability = experiment(hat=hat, expected_balls={"red": 1, "green": 2}, num_balls_drawn=4, num_experiments=1000)
print(probability)