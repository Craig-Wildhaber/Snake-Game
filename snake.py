from turtle import Turtle
START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.limbs = []
        self.create_default_snake()
        self.head = self.limbs[0]

    def create_default_snake(self):
        for position in START_POSITIONS:
            self.add_limb(position)

    def add_limb(self, positions):
        new_limb = Turtle(shape="square", )
        new_limb.color("green")
        new_limb.penup()
        new_limb.setposition(positions)
        self.limbs.append(new_limb)

    def eat_fruit(self):
        self.add_limb(self.limbs[-1].position())

    def move(self):
        for limb_num in range(len(self.limbs) - 1, 0, -1):
            new_x = self.limbs[limb_num - 1].xcor()
            new_y = self.limbs[limb_num - 1].ycor()
            self.limbs[limb_num].goto(new_x, new_y)
        self.limbs[0].forward(MOVE_DISTANCE)

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
