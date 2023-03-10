from turtle import Screen
from player import Player

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title("Pong")

player1 = Player((350, 0))
player2 = Player((-350, 0))


screen.listen()
screen.onkey(fun=player1.up, key='Up')
screen.onkey(fun=player1.down, key="Down")
screen.onkey(fun=player2.up, key='w')
screen.onkey(fun=player2.down, key="s")


screen.exitonclick()