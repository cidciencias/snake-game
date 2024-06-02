import time
from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
segments_list = []

for position in starting_positions:
    new_segment = Turtle("square")
    new_segment.penup()
    new_segment.color("white")
    new_segment.goto(position)
    segments_list.append(new_segment)


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments_list) - 1, 0, -1):
        new_x = segments_list[seg_num - 1].xcor()
        new_y = segments_list[seg_num - 1].ycor()
        segments_list[seg_num].goto(new_x, new_y)
    segments_list[0].forward(20)
    segments_list[0].left(90)





screen.exitonclick()