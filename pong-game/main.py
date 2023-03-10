from turtle import Screen
from player import Player
from ball import Ball
import time

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")
screen.tracer(0)

player1 = Player((350, 0))
player2 = Player((-350, 0))
ball = Ball()


screen.listen()
screen.onkey(fun=player1.up, key='Up')
screen.onkey(fun=player1.down, key="Down")
screen.onkey(fun=player2.up, key='w')
screen.onkey(fun=player2.down, key="s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with top wall or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -277:
        # Needs to bounce
        ball.bounce_y()
    
    # Detect collision with the players
    if ball.distance(player1) < 50 and ball.xcor() > 320 or ball.distance(player2) < 50 and ball.xcor() < -320:
        ball.bounce_x()


screen.exitonclick()