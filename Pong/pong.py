
import turtle
import os

WIDTH = 800
HEIGHT = 600

win = turtle.Screen()
win.title("Pong")
win.bgcolor("black")
win.setup(width=WIDTH, height=HEIGHT)
win.tracer(0)

# * Score
score_a = 0
score_b = 0


# * Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_a.penup()
paddle_a.goto(-350, 0)


# * Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=5, stretch_len=0.5)
paddle_b.penup()
paddle_b.goto(350, 0)

# * Ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.04
ball.dy = 0.04

# * Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A: {score_a}  |  PlayerB: {score_b}", align="center", font=("Courier", 18, "bold"))


# * Functions
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)


def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)


def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)
    

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# * Keybord binding


win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeypress(paddle_b_down, "Down")


# * Main game loop
while True:
    win.update()

    # * Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # * Border checking
    if ball.ycor() > (280):
        ball.sety(280)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.ycor() < (-280):
        ball.sety(-280)
        ball.dy *= -1
        os.system("aplay bounce.wav&")

    if ball.xcor() > (400):
        ball.goto(0, 0)
        ball.dx *= -1
        score_a += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  |  PlayerB: {score_b}", align="center", font=("Courier", 18, "bold"))


    if ball.xcor() < (-400):
        ball.goto(0, 0)
        ball.dx *= -1
        score_b += 1
        pen.clear()
        pen.write(f"Player A: {score_a}  |  PlayerB: {score_b}", align="center", font=("Courier", 18, "bold"))


    # * Paddle and ball collision
    if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
        ball.setx(340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
        ball.setx(-340)
        ball.dx *= -1
        os.system("aplay bounce.wav&")