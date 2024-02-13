import turtle
import os

# Initialize scores
player_a_score = 0
player_b_score = 0

# Create a window
window = turtle.Screen()
window.title("The Pong Game")   
window.bgcolor("green")
window.setup(width=800, height=600)
window.tracer(0)

# Create left paddle
left_paddle = turtle.Turtle()
left_paddle.speed(0)
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-350, 0)

# Create right paddle
right_paddle = turtle.Turtle()
right_paddle.speed(0)
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(350, 0)

# Create the ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("red")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.175
ball.dy = 0.175

# Create a pen for the score
pen = turtle.Turtle()
pen.speed(0)
pen.color("blue")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Player A: 0  Player B: 0", align="center", font=("Arial", 24, "normal"))

# Move left paddle up
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

# Move left paddle down
def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

# Move right paddle up
def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

# Move right paddle down
def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

# Keyboard bindings
window.listen()
window.onkeypress(left_paddle_up, "w")
window.onkeypress(left_paddle_down, "s")
window.onkeypress(right_paddle_up, "Up")
window.onkeypress(right_paddle_down, "Down")

while True:
    window.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.dy *= -1

    # Ball and paddle collisions
    if (
        (ball.xcor() > 340 and ball.xcor() < 350)
        and (ball.ycor() < right_paddle.ycor() + 50 and ball.ycor() > right_paddle.ycor() - 50)
    ):
        ball.color("blue")
        ball.setx(340)
        ball.dx *= -1
        os.system("afplay paddle.wav&")

    elif (
        (ball.xcor() < -340 and ball.xcor() > -350)
        and (ball.ycor() < left_paddle.ycor() + 50 and ball.ycor() > left_paddle.ycor() - 50)
    ):
        ball.color("red")
        ball.setx(-340)
        ball.dx *= -1
        os.system("afplay paddle.wav&")

    # Scoring
    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_a_score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_a_score, player_b_score), align="center", font=("Arial", 24, "normal"))
        os.system("afplay wallhit.wav&")

    elif ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx *= -1
        player_b_score += 1
        pen.clear()
        pen.write("Player A: {}  Player B: {}".format(player_a_score, player_b_score), align="center", font=("Arial", 24, "normal"))
        os.system("afplay wallhit.wav&")
