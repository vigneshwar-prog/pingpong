import turtle
import winsound

win=turtle.Screen()
win.title("Ping Pong")
win.bgcolor("Black")
win.setup(width=840, height=630)
win.tracer(0) 
def reset():
    turtle.resetscreen()

#score
score_a=0
score_b=0

#Boder_Box
#left
box_left=turtle.Turtle()
box_left.speed(0)
box_left.shape("square")
box_left.color("white")
box_left.shapesize(stretch_wid=30, stretch_len=0.5)
box_left.penup()
box_left.goto(-400,0)

#right
box_right=turtle.Turtle()
box_right.speed(0)
box_right.shape("square")
box_right.color("white")
box_right.shapesize(stretch_wid=30, stretch_len=0.5)
box_right.penup()
box_right.goto(400,0)

#up
box_up=turtle.Turtle()
box_up.speed(0)
box_up.shape("square")
box_up.color("white")
box_up.shapesize(stretch_wid=0.5, stretch_len=40)
box_up.penup()
box_up.goto(0,-300)

#down
box_down=turtle.Turtle()
box_down.speed(0)
box_down.shape("square")
box_down.color("white")
box_down.shapesize(stretch_wid=0.5, stretch_len=40)
box_down.penup()
box_down.goto(0,300)


#paddle A
pad_a = turtle.Turtle()
pad_a.speed(0)
pad_a.shape("square")
pad_a.color("white")
pad_a.shapesize(stretch_wid=5, stretch_len=1)
pad_a.penup()
pad_a.goto(-350,0)

#paddle B
pad_b = turtle.Turtle()
pad_b.speed(0)
pad_b.shape("square")
pad_b.color("white")
pad_b.shapesize(stretch_wid=5, stretch_len=1)
pad_b.penup()
pad_b.goto(350,0)

#ball
ball = turtle.Turtle()
ball.speed(0)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0,0)
ball.dx = 1.5
ball.dy = 1.5

#pen
pen=turtle.Turtle()
pen.speed(0)
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0,240)
pen.write("Player A: 0 Player B: 0",align="center", font=("Courier",24,"normal"))

e_pen=turtle.Turtle()
e_pen.speed(0)
e_pen.color("white")
e_pen.penup()
e_pen.hideturtle()
e_pen.goto(0,0)


#functions
def pad_a_up():
    y=pad_a.ycor()
    y+=50
    pad_a.sety(y)
def pad_a_down():
    y=pad_a.ycor()
    y-=50
    pad_a.sety(y)
def pad_b_up():
    y=pad_b.ycor()
    y+=50
    pad_b.sety(y)
def pad_b_down():
    y=pad_b.ycor()
    y-=50
    pad_b.sety(y)
def exit():
    turtle.Screen().bye()

def winning():

    while(1):
        if(w==1):
            e_pen.write("Congo !! Player A Won the Game !\nPlay Again 'y' or 'n' ",align="center", font=("Courier",24,"normal"))
            #e_pen.write("Play Again 'y' or 'n' ",align="bottom", font=("Courier",24,"normal"))
        if(w==2):
            e_pen.write("Congo !! Player B Won the Game !\nPlay Again 'y' or 'n' ",align="center", font=("Courier",24,"normal"))
            #e_pen.write("Play Again 'y' or 'n' ",align="bottom", font=("Courier",24,"normal"))
        win.listen()
        win.onkeypress(reset,"y")
        win.onkeypress(exit,"n")


    

#keyboard
win.listen()
win.onkeypress(pad_a_up,"w")
win.onkeypress(pad_a_down,"s")
win.onkeypress(pad_b_up,"Up")
win.onkeypress(pad_b_down,"Down")



#main game loop
while(1):
    win.update()
    
    #ball movement
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)
    
    #border
    if ball.ycor() >290:
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        ball.sety(290)
        ball.dy *=-1
    if ball.ycor() <-290:
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        ball.sety(-290)
        ball.dy *=-1
    if ball.xcor() >390:
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        ball.setx(390)
        score_a+=1
        #ball.goto(0,0)
        ball.dx *=-1
        pen.clear()
        pen.write("Player A: %d Player B: %d"%(score_a,score_b),align="center", font=("Courier",24,"normal"))
    if ball.xcor() < -390:
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        #ball.goto(0,0)
        score_b+=1
        ball.setx(-390)
        ball.dx *=-1
        pen.clear()
        pen.write("Player A: %d Player B: %d"%(score_a,score_b),align="center", font=("Courier",24,"normal"))

    #paddle movement
    if pad_a.ycor() > 250:
        pad_a.sety(-250)
    if pad_a.ycor() < -250:
        pad_a.sety(250)
    if pad_b.ycor() > 250:
        pad_b.sety(-250)
    if pad_b.ycor() < -250:
        pad_b.sety(250)


    #paddle and ball collision

    if( ball.xcor()>340 and ball.xcor() < 350) and (ball.ycor() < pad_b.ycor() + 40 and ball.ycor() > pad_b.ycor() - 40 ):
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        ball.setx(340)
        ball.dx*=-1
    if( ball.xcor()<-340 and ball.xcor() > -350) and (ball.ycor() < pad_a.ycor() + 40 and ball.ycor() > pad_a.ycor() - 40 ):
        winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        ball.setx(-340)
        ball.dx*=-1

    if(score_a==10 ):
        turtle.clear()
        w=1
        winsound.PlaySound('win.wav',winsound.SND_ASYNC)
        winning()
        break

    if(score_b==10): 
        turtle.clear()
        w=2
        winsound.PlaySound('win.wav',winsound.SND_ASYNC)
        winning()
        break







    
