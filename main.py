from turtle import Turtle, Screen

timmy = Turtle()

screen = Screen()


def move_forward():
    timmy.forward(10)


def move_backward():
    timmy.backward(10)


def clock_wise():
    timmy.right(10)


def anti_clock_wise():
    timmy.left(10)


def clear():
    timmy.clear()
    timmy.penup()
    timmy.home()
    timmy.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=clock_wise)
screen.onkey(key="d", fun=anti_clock_wise)
screen.onkey(key="c", fun=clear)
screen.exitonclick()
