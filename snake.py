from turtle import Turtle
START_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class MySnake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):

        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        body = Turtle()
        body.shape("square")
        body.color("white")
        body.penup()
        body.goto(position)
        self.segments.append(body)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    # add a new segment to the snake
    def extend(self):
        self.add_segment(self.segments[-1].position())


    def move_forward(self):
        for body_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[body_num - 1].xcor()
            new_y = self.segments[body_num - 1].ycor()
            self.segments[body_num].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
