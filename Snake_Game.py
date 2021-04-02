import turtle
import time
import random

score=0
high_score=0
delay=0.1

# Setting Up The Screen
screen=turtle.Screen()
screen.title("SNAKE GAME !!")
screen.bgcolor('black')
screen.setup(width=450, height=450)
screen.tracer(0)

# Snake Head
head=turtle.Turtle()
head.shape('square')
head.speed(0)
head.color('white')
head.fillcolor('light green')
head.penup()
head.goto(-50,-50)
head.direction='stop'

# Snake Food
food=turtle.Turtle()
food.speed(0)
food.shape('circle')
food.color('deep pink')
food.penup()
food.goto(0,100)

# Scoreboard
scores=turtle.Turtle()
scores.speed(0)
scores.shape('circle')
scores.color('SKY BLUE')
scores.penup()
scores.goto(2,190)
scores.hideturtle()
scores.write("SCORE: 0   HIGHEST SCORE: 0",font=("tahoma",10,"bold"))

# Snake Movement Functions
def go_up():
    if head.direction!="down":
        head.direction="up"
def go_down():
    if head.direction!="up":
        head.direction="down"
def go_right():
    if head.direction!="left":
        head.direction="right"
def go_left():
    if head.direction!="right":
        head.direction="left"
def move():
    if head.direction=="up":
        y=head.ycor()
        head.sety(y+20)
    if head.direction=="down":
        y=head.ycor()
        head.sety(y-20)
    if head.direction=="right":
        x=head.xcor()
        head.setx(x+20)
    if head.direction=="left":
        x=head.xcor()
        head.setx(x-20)


# Key Bindings
screen.listen()
screen.onkeypress(go_up,"8")
screen.onkeypress(go_down,"2")
screen.onkeypress(go_right,"6")
screen.onkeypress(go_left,"4")

segment =[]

while True:
    screen.update()

    #Check collision with the border area
    if head.xcor()>205:
        head.setx(-205)
    if head.xcor()<-205:
        head.setx(205)
    if head.ycor()>205:
        head.sety(-205)
    if head.ycor()<-205:
        head.sety(205)

    # Check Collision with the food
    if head.distance(food)<20:
        # Moving the food to a new place
        x=random.randint(-205,205)
        y=random.randint(-205,205)
        food.goto(x,y) 

        # Increasing the score
        score+=10

        # Changing the delay
        delay-=0.001

        # Increasing the length of the snake
        body=turtle.Turtle()
        body.speed(0)
        body.penup()
        body.shape('square')
        body.color('white')
        body.fillcolor('light green')
        segment.append(body)
         
        # Updating the highest score
        if score>high_score:
            high_score=score
        scores.clear()
        scores.write("SCORE: {}  HIGHEST SCORE: {}".format(score,high_score),font=("tahoma",10,"bold"))

    # Moving the segments of the body 
    for index in range(len(segment)-1,0,-1):
        x=segment[index-1].xcor()
        y=segment[index-1].ycor()
        segment[index].goto(x,y)
    if len(segment)>0:
        x=head.xcor()
        y=head.ycor()
        segment[0].goto(x,y)
    move()

    # Checking Collision with the snake body
    for body in segment:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction='stop'
            for body in segment:
                body.hideturtle()
            segment.clear()

            score=0
            delay=0.1

            # Updating Scoreboard
            scores.clear()
            scores.write("SCORE: {}  HIGHEST SCORE: {}".format(score,high_score),font=("tahoma",10,"bold"))
    time.sleep(delay)
screen.mainloop()
