from turtle import Turtle, Screen 
import time
from snake import Snake
from food import Food
from scoreboard import Score 



screen = Screen()
screen.setup(width = 600 , height = 600 )
screen.bgcolor("black")
screen.title("My Snake Game")

snake = Snake()
food = Food()
score = Score()

screen.listen()
screen.onkey(snake.up,"Up")
screen.onkey(snake.down,"Down")
screen.onkey(snake.left,"Left")
screen.onkey(snake.right,"Right")


game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    # detect collision with food
    # the circle is 10,10 so this check 
    # if the snake is wihtin that range of the food 
    # if it is then the snake has eaten the food

    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        score.increase_score()

    if snake.head.xcor() >280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        game_is_on = False
        score.game_over()   

    #detect collision with tail 
    for segment in snake.snake_position[1:]:
        if  snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

    screen.update()




screen.exitonclick()



