from turtle import Turtle
SHAPE = [(0,0),(-20,0), (-40,0)] 
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_position = []
        self.create_snake()
        self.head = self.snake_position[0]

    def create_snake(self):
        for position in SHAPE:
            self.add_segment(position)



    def add_segment(self, position):
        t = Turtle()
        t.shape("square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.snake_position.append(t)

    def extend(self):
        self.add_segment(self.snake_position[-1].position())


    def move(self):
        for seg_num in range(len(self.snake_position) -1 , 0 , -1):
            new_x = self.snake_position[seg_num -1 ].xcor()
            new_y = self.snake_position[seg_num -1 ].ycor()
            self.snake_position[seg_num].goto(new_x , new_y)
        self.head.forward(MOVING_DISTANCE)


    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(DOWN)

    def left(self):
        self.head.setheading(LEFT)

    def right(self):
        self.head.setheading(RIGHT)

    