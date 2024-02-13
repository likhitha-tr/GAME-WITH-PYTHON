import turtle
import random

class SnakeGame:
    def __init__(self, width=500, height=500, food_size=10, delay=100):
        self.w = width
        self.h = height
        self.food_size = food_size
        self.delay = delay
        self.offsets = {"up": (0, 20), "down": (0, -20), "left": (-20, 0), "right": (20, 0)}
        self.screen = turtle.Screen()
        self.screen.setup(self.w, self.h)
        self.screen.title("Snake")
        self.screen.bgcolor("blue")
        self.screen.setup(500, 500)
        self.screen.tracer(0)
        self.pen = turtle.Turtle("square")
        self.pen.penup()
        self.food = turtle.Turtle()
        self.food.shape("square")
        self.food.color("yellow")
        self.food.shapesize(self.food_size / 20)
        self.food.penup()
        self.reset()

    def reset(self):
        self.snake = [[0, 0], [0, 20], [0, 40], [0, 60], [0, 80]]
        self.snake_dir = "up"
        self.food_position = self.get_random_food_position()
        self.food.goto(self.food_position)
        self.move_snake()

    def move_snake(self):
        new_head = self.snake[-1].copy()
        new_head[0] = self.snake[-1][0] + self.offsets[self.snake_dir][0]
        new_head[1] = self.snake[-1][1] + self.offsets[self.snake_dir][1]

        if new_head in self.snake[:-1]:
            self.reset()
        else:
            self.snake.append(new_head)

            if not self.food_collision():
                self.snake.pop(0)

            if self.snake[-1][0] > self.w / 2:
                self.snake[-1][0] -= self.w
            elif self.snake[-1][0] < -self.w / 2:
                self.snake[-1][0] += self.w
            elif self.snake[-1][1] > self.h / 2:
                self.snake[-1][1] -= self.h
            elif self.snake[-1][1] < -self.h / 2:
                self.snake[-1][1] += self.h

            self.pen.clearstamps()

            for segment in self.snake:
                self.pen.goto(segment[0], segment[1])
                self.pen.stamp()

            self.screen.update()
            turtle.ontimer(self.move_snake, self.delay)

    def food_collision(self):
        if self.get_distance(self.snake[-1], self.food_position) < 20:
            self.food_position = self.get_random_food_position()
            self.food.goto(self.food_position)
            return True
        return False

    def get_random_food_position(self):
        x = random.randint(-self.w / 2 + self.food_size, self.w / 2 - self.food_size)
        y = random.randint(-self.h / 2 + self.food_size, self.h / 2 - self.food_size)
        return x, y

    def get_distance(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
        return distance

    def go_up(self):
        if self.snake_dir != "down":
            self.snake_dir = "up"

    def go_right(self):
        if self.snake_dir != "left":
            self.snake_dir = "right"

    def go_down(self):
        if self.snake_dir != "up":
            self.snake_dir = "down"

    def go_left(self):
        if self.snake_dir != "right":
            self.snake_dir = "left"

    def start(self):
        self.screen.listen()
        self.screen.onkey(self.go_up, "Up")
        self.screen.onkey(self.go_right, "Right")
        self.screen.onkey(self.go_down, "Down")
        self.screen.onkey(self.go_left, "Left")
        turtle.done()

# Instantiate the game and start it
game = SnakeGame()
game.start()
