import copy
import random

class Hat:
    def __init__(self, **kwargs):
        self.contents = []
        for color, count in kwargs.items():
            self.contents.extend([color] * count)
            
    def draw(self, num_balls):
        # If requesting more balls than available, return all balls
        if num_balls >= len(self.contents):
            all_balls = self.contents
            self.contents = []  # Empty the hat
            return all_balls
        
        # Randomly draw balls
        drawn_balls = []
        for _ in range(num_balls):
            ball_idx = random.randrange(len(self.contents))
            drawn_balls.append(self.contents.pop(ball_idx))
        
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    successful_experiments = 0
    
    for _ in range(num_experiments):
        # Create a deep copy of the hat for each experiment
        hat_copy = copy.deepcopy(hat)
        
        # Draw balls
        drawn_balls = hat_copy.draw(num_balls_drawn)
        
        # Count the drawn balls
        drawn_counts = {}
        for ball in drawn_balls:
            drawn_counts[ball] = drawn_counts.get(ball, 0) + 1
        
        # Check if we got at least the expected number of each ball
        success = True
        for color, count in expected_balls.items():
            if color not in drawn_counts or drawn_counts[color] < count:
                success = False
                break
        
        if success:
            successful_experiments += 1
    
    # Calculate and return probability
    return successful_experiments / num_experiments

# Test the fixed draw method
if __name__ == "__main__":
    # Test case 1: Drawing exactly the number of balls in the hat
    hat1 = Hat(red=2, blue=1)
    print("Hat 1 initial contents:", hat1.contents)
    drawn = hat1.draw(3)
    print("Drawing 3 balls (exact):", drawn)
    print("Remaining balls:", hat1.contents)
    
    # Test case 2: Drawing more balls than available
    hat2 = Hat(red=2, blue=1)
    print("\nHat 2 initial contents:", hat2.contents)
    drawn = hat2.draw(5)
    print("Drawing 5 balls (more than available):", drawn)
    print("Remaining balls:", hat2.contents)
    
    # Test case 3: Drawing fewer balls than available
    hat3 = Hat(red=2, blue=1)
    print("\nHat 3 initial contents:", hat3.contents)
    drawn = hat3.draw(2)
    print("Drawing 2 balls (fewer than available):", drawn)
    print("Remaining balls:", hat3.contents)