# CS-UY 1114
# Final project

import turtle
import time
import os
import math


userx = 0

enemies = [(100,200, "left"), (200,250, "left"), (0, 100, "right"),]

bullets = []

gameover = False

bulletSpeed = 15

playerSpeed = 20

enemySpeed = 5

score = 0


def draw_frame():
    """
    signature: () -> NoneType
    Given the current state of the game in
    the global variables, draw all visual
    elements on the screen: the player's ship,
    the enemies, and the bullets.
    Please note that this is your only function
    where drawing should happen (i.e. the only
    function where you call functions in the
    turtle module). Other functions in this
    program merely update the state of global
    variables.
    This function also should not modify any
    global variables.
    Hint: write this function first!
    """
    turtle.setheading(90)
    global score
    
    #the scene
    mainScreen = turtle.Screen()
    mainScreen.bgcolor("black")
    mainScreen.title("Rachel's Space Invaders")
    mainScreen.bgpic("spaceinvadbg.jpg")

    #the player
    turtle.penup()
    turtle.color("red")
    turtle.speed(50)
    turtle.setposition(userx,-100)
    turtle.pendown()
    turtle.fd(20)
    turtle.left(120)
    turtle.fd(20)
    turtle.left(120)
    turtle.fd(20)
    turtle.left(60)
    turtle.penup()

    

    #the enemies
    for i in range(len(enemies)):
        turtle.setposition(enemies[i][0:2])
        turtle.pendown()
        turtle.color("blue")
        turtle.circle(10)
        turtle.speed(50)
        turtle.penup()
        turtle.hideturtle()

    #the bullet
    for bullet in bullets:
        turtle.setposition(bullet[0], bullet[1])
        turtle.color("yellow")
        turtle.pendown()
        turtle.fd(10)
        turtle.left(90)
        turtle.fd(10)
        turtle.left(90)
        turtle.fd(10)
        turtle.left(90)
        turtle.fd(10)
        turtle.left(90)
        turtle.penup()
        turtle.speed(0)
        turtle.shapesize(0.5, 0.5)
        turtle.hideturtle()

    #the score
    turtle.setposition(-250, 250)
    turtle.color("green")
    turtle.write(score, font = ("Arial", 30, "normal"))
    
    if gameover == True:
        turtle.setposition(0,0)
        turtle.write("gameover, your score is " + str(score), move = False, align = "center", font = ("Arial",20,"normal"))
                  

def key_left():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the player's ship
    appropriately by modifying the variable
    userx.
    """
    global userx
    global playerSpeed
    userx -= playerSpeed
    if float(userx) < -250:
        userx = -250
    
    

def key_right():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the left arrow. It should
    adjust the position of the player's ship
    appropriately by modifying the variable
    user1x.
    """
    global userx
    global playerSpeed
    userx += playerSpeed
    if float(userx) > 250:
        userx = 250
    

def key_space():
    """
    signature: () -> NoneType
    This function is called by turtle whenever
    the user press the space key. It should
    add a new bullet to the list of bullets.
    """
    global bullets
    global userx

    bullets.append((userx,-90))

def physics():
    """
    signature: () -> NoneType
    Update the state of the game world, as
    stored in the global variables. Here, you
    should check the positions of the bullets,
    and remove them if they go off the screen
    or collide with an enemy. In the later case
    you should also remove the enemy. That is,
    given the current position of the bullets,
    calculate their position in the next frame.
    """
    global bullets
    global enemies
    global enemySpeed
    global bulletSpeed
    global x_val
    global y_val
    global StateofBullet
    global score
    global gameover
    
    for i in range(len(bullets)):
        x_val = bullets[i-1][0]
        y_val = bullets[i-1][1]
    
        y_val += bulletSpeed
        bullets[i-1] = (x_val, y_val)
    
        if bullets[i-1][1] > 300:
            #find the tuple of the bullet and remove it
            off_bullet = bullets.pop(i)
          

        
    for enemy in enemies:
        for bullet in bullets:
            t1_x = enemy[0]
            t1_y = enemy[1]
            t2_x = bullet[0]
            t2_y = bullet[1]
            distance = math.sqrt(math.pow(t1_x-t2_x,2)+math.pow(t1_y-t2_y,2))
            
            if distance <= 20:
                enemies.remove(enemy)
                bullets.remove(bullet)
                score += 10
                
    
    for enemy in enemies:
        t1_x = enemy[0]
        t1_y = enemy[1]
        t2_x = userx
        t2_y = -100
        distance2 = math.sqrt(math.pow(t1_x-t2_x,2)+math.pow(t1_y-t2_y,2))
            
        if distance2 <= 20:
            gameover = True
            print("Gameover, your score is", score)

        

    


def ai():
    
    """
    signature: () -> NoneType
    Perform the 'artificial intelligence' of
    the game, by updating the position of the
    enemies, stored in the enemies global
    variable. That is, given their current
    position, calculate their position
    in the next frame.
    If the enemies reach the player's ship,
    you should set the gameover variable
    to True. Also, if there are no more
    enemies left, set gameover to True.
    """
    global enemies
    global gameover
    global enemySpeed

   
    for i in range(len(enemies)):
        x_val_position = 0 # x position index
        y_val_position = 1 # y position index
        direction_position = 2 #left or right
        position = 0
        x_val = enemies[i][0] #x value of bullet
        y_val = enemies[i][1] #y value of bullet
        
        #change direction speed
        if enemies[i][direction_position] == "left":
            x_val -= enemySpeed
            enemies[i] = (x_val, y_val, "left")
            
            if x_val < -250:
                #enemies[i][direction_position] = "right"
                y_val -= 40
                enemies[i] = (x_val, y_val, "right")

            
        elif enemies[i][direction_position] == "right":
            x_val += enemySpeed
            enemies[i] = (x_val, y_val, "right")
            
            if x_val > 250:
                #enemies[i][direction_position] = "left"
                y_val -= 40
                enemies[i] = (x_val, y_val, "left")


            #replace y val of bullet

    position += 1

    if len(enemies) == 0:
        gameover = True

    #determine if reach player w distance

           

def reset():
    """
    signature: () -> NoneType
    This function is called when your game starts.
    It should set initial value for all the
    global variables.
    """
    global enemies
    global bullets
    global userx
    global gameover
    global playerSpeed
    global enemySpeed
    global StateofBullet
    global score


    userx = 0
    playerSpeed = 20
    enemySpeed = 5
    bulletSpeed = 5
    enemies = [(100,200, "left"), (200,250, "left"), (0, 100, "right"), (0,200,"right"),(150,90,"left")]
    bullets = []
    gameover = False
    StateofBullet = "notfired"
    score = 0


def main():
    """
    signature: () -> NoneType
    Run the game. You shouldn't need to
    modify this function.
    """
    draw_frame()

    score = 0
    
    turtle.tracer(0,0)
    turtle.hideturtle()
    turtle.onkey(key_left, "Left")
    turtle.onkey(key_right, "Right")
    turtle.onkey(key_space, "space")
    turtle.listen()
    reset()
    while not gameover:
        physics()
        ai()
        turtle.clear()
        draw_frame()
        turtle.update()
        time.sleep(0.05)
        

        

main()
