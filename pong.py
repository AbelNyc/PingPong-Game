import turtle
import playsound
import os #operating system module

windows_h = turtle.Screen()  #create windows screem 
windows_h.title("Pong by Abel")
windows_h.bgcolor("blue")
windows_h.setup(width=800,height=600)
windows_h.tracer(0) #help speed up the game

#paddle A
paddle_a=turtle.Turtle()
paddle_a.speed(0)# set the speed to the max possible
paddle_a.shape("square")
paddle_a.color("grey")
paddle_a.shapesize(stretch_wid=5,stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350,0)

#paddle B
paddle_b=turtle.Turtle()
paddle_b.speed(0)# set the speed to the max possible
paddle_b.shape("square")
paddle_b.color("grey")
paddle_b.shapesize(stretch_wid=5,stretch_len=1)
paddle_b.penup()
paddle_b.goto(350,0)

#ball
ball=turtle.Turtle()
ball.speed(0)# set the speed to the max possible
ball.shape("square")
ball.color("grey")
ball.penup()
ball.goto(0,0)
ball.dx=.1 # moves by two pixels everytime
ball.dy=-.1

#keeping tabs of the score 

score_1=0
score_2=0

#scoring system

pen=turtle.Turtle()
pen.speed(0)
pen.color("yellow")
pen.penup()
pen.hideturtle()
pen.goto(0,260)
pen.write("Player 1: 0   Player 2: 0",align="center",font=("Times New Romans",24,"normal"))

#functions for paddle_a
def paddle_a_up():
    y=paddle_a.ycor() #returns the y coordinate up
    y+=20
    paddle_a.sety(y)

def paddle_a_down():
    y=paddle_a.ycor() #returns the y coordinate down
    y-=20
    paddle_a.sety(y)

#functions for paddle_b
def paddle_b_up():
    y=paddle_b.ycor() #returns the y coordinate up
    y+=20
    paddle_b.sety(y)

def paddle_b_down():
    y=paddle_b.ycor() #returns the y coordinate dwon
    y-=20
    paddle_b.sety(y)

#moving the paddle 
#keyboard input for paddle_a
windows_h.listen()
windows_h.onkeypress(paddle_a_up,"w") # when the user presses w call the paddle_up function 
windows_h.onkeypress(paddle_a_down,"s") # when the user presses w call the paddle_down function 



#keyboard input for paddle_b
windows_h.listen()
windows_h.onkeypress(paddle_b_up,"9") # when the user presses w call the paddle_up function 
windows_h.onkeypress(paddle_b_down,"0") # when the user presses w call the paddle_down function 



while True:
    windows_h.update()

    #move the ball
    ball.setx(ball.xcor()+ball.dx) # keep moving in x direction 
    ball.sety(ball.ycor()+ball.dy) # keep moving in y direction 




    #border checking
    if ball.ycor()>290: #if ycoordinate is > 290 then reset back to 290 it 
        ball.sety(290)
        ball.dy*=-1  #reverses the direction
        playsound.playsound("bounce.wav")
        #playing the sound

    if ball.ycor()<-290:
        ball.sety(-290)
        ball.dy*=-1
        playsound.playsound("bounce.wav")
    
    if ball.xcor()>390:
        ball.goto(0,0)
        ball.dx*=-1
        playsound.playsound("bounce.wav")
        score_1+=1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1,score_2),align="center",font=("Times New Romans",24,"normal")) #updating the score 



    if ball.xcor()<-390:
        ball.goto(0,0)
        ball.dx*=-1
        playsound.playsound("bounce.wav")
        score_2+=1
        pen.clear()
        pen.write("Player 1: {}  Player 2: {}".format(score_1,score_2),align="center",font=("Times New Romans",24,"normal")) #updating the score 



    #paddle and ball collision on the right side
    if (ball.xcor()>340 and ball.xcor()<350) and (ball.ycor()<paddle_b.ycor()+50 and ball.ycor()>paddle_b.ycor()-50):
       ball.setx(340)
       ball.dx *=-1

    #paddle and ball collision on the left side
    if (ball.xcor()<- 340 and ball.xcor()>-350) and (ball.ycor()<paddle_a.ycor()+50 and ball.ycor()>paddle_a.ycor()-50):
       ball.setx(-340)
       ball.dx *=-1

