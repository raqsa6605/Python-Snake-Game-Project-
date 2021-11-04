import turtle
import time
import random


delay = 0.1

#Score
score = 0
high_score = 0


# Set up the Screen
window = turtle.Screen()
#Setting Title
window.title("Snake Game by Acsah") 
#Setting Backgroung Color
window.bgcolor("yellow")
# Setting Screen Size
window.setup(width=500, height=500)
# It will turn off the animation on the screen
window.tracer(0)
#Snake Head
head = turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("Green")
head.penup()
head.goto(0,0)
head.direction = "stop"

# Snake Food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("White")
food.penup()
food.goto(0,100)

segments = []

#Pen
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("black")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write("Score: 0  High Score: 0", align=("center"), font=("Ariel", 24, "normal"))


#Functionss
def go_up():
    if head.direction != "down":
        head.direction = "up"
def go_down():
     if head.direction != "up":
        head.direction = "down"
def go_left():
     if head.direction != "right":
        head.direction = "left"
def go_right():
     if head.direction != "left":
        head.direction = "right"    

def move():
    if head.direction == "up":
        y= head.ycor()
        head.sety(y + 20)
    
    if head.direction == "down":
        y= head.ycor()
        head.sety(y - 20)
    
    if head.direction == "left":
        x= head.xcor()
        head.setx(x - 20)
    
    if head.direction == "right":
        x= head.xcor()
        head.setx(x + 20)    
# Keyboard Bindings
window.listen()
window.onkeypress(go_up, "w")
window.onkeypress(go_down, "s")
window.onkeypress(go_left, "a")
window.onkeypress(go_right, "d")

#Main Game loop
while True:
    window.update()
    
    #Check for a collision with border
    if head.xcor() > 240 or head.xcor() < -240 or head.ycor() > 240 or head.ycor() < -240:
        time.sleep(1)
        head.goto(0,0)
        head.direction = "stop"
        
    #Hide the Segments
    for segment in segments:
        segment.goto(1000, 1000)
            
    #Clear the segments list
    segments.clear()
    
    # Reset the score
    score = 0
    
    pen.clear()
    pen.write("Score: {}  High Score: {}".format(score, high_score), align=("center"), font=("Ariel", 24, "normal")) 
    
    #Check for a collision with food
    if head.distance(food) < 20:
        #Move the f0od at some spot on the screen
        x = random.randint(-240,240)
        y = random.randint(-240, 240)
        food.goto(x, y)
        
        #Add a Segment
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("red")
        new_segment.penup()
        segments.append(new_segment)
        
        # Shorten the dalay
        delay -= 0.001
        # Increase Score
        score += 10
        
        if score > high_score:
            high_score = score
        pen.clear()
        pen.write("Score: {}  High Score: {}".format(score, high_score), align=("center"), font=("Ariel", 24, "normal"))  
        
    
    # Move the end segments first in reverse
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)
        
    #Move segment 0 to where the head is
    if len(segments) > 0:
        x= head.xcor()
        y= head.ycor()
        segments[0].goto(x, y)
    
    move()
    
    #Check for head collision
    for segment in segments:
        if segment.distance(head)< 20:
            time.sleep(1)
            head.got(0,0)
            head.direction = "stop"
            
            #Hide the Segments
            for segment in segments:
                segment.goto(1000, 1000)
            
            #Clear the segments list
            segments.clear()        
            # Reset the score
            score = 0
            
            # Reset the dalay
            delay = 0.1
            pen.clear()
            pen.write("Score: {}  High Score: {}".format(score, high_score), align=("center"), font=("Ariel", 24, "normal")) 
    
    time.sleep(delay)
#This will keep the window open for us
window.mainloop()
