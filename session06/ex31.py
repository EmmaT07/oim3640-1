import turtle
from turtle_shape import square

turtle.speed(0)


def spiral(t, n):
    """
    draw a spiral shape - that is drawing a square multiple times,
    after one square, turn 5 degrees
    t: a turtle
    n: int, number of squares to draw for the spiral
    """
    # pseudo code
    # 1. prompt user to ask for a length value, store it into a variable
    # 2. convert variable to a int
    # 2. repeat the following task/steps n times
    #      1. draw a square with length
    #      2. turn right 5 degrees
    #      3. increase length by 4

    length = input()
    for i in range(60):
        square(t, length)
        t.right(5)
        length = length + 4


leo = turtle.Turtle()
spiral(leo, 10)
