import turtle
import math
import random

def initalize(p):
    turtle.speed(0)
    turtle.pencolor("black")
    turtle.penup()
    turtle.goto(-10*p,10*p)

def draw_pixel(p,color):
    turtle.pendown()
    turtle.fillcolor(color)
    turtle.begin_fill()
    i = 0
    while i < 4:
        turtle.forward(p)
        turtle.right(90)
        i = i+1
    turtle.end_fill()
    turtle.penup()

def draw_grid(p):
    initalize(p)
    i = 0
    while i < 21:
        turtle.pendown()
        turtle.forward(20*p)
        turtle.penup()
        turtle.goto(-10*p,(10-i-1)*p)
        i=i+1
    initalize(p)
    turtle.right(90)
    i = 0
    while i < 21:
        turtle.pendown()
        turtle.forward(20*p)
        turtle.penup()
        turtle.goto((-10+1+i)*p,10*p)
        i=i+1
    turtle.setheading(0)

def move(column,row,p):
    turtle.goto((column-10)*p,(10-row)*p)

def draw_row(column,row,length,p,color):
    move(column,row,p)
    i=0
    while(i<length):
        draw_pixel(p,color)
        turtle.forward(p)
        i=i+1
        #print(turtle.position())
        if(math.ceil(turtle.xcor())>=10*p):
            #print(str(10*p) + " " + str(turtle.xcor()))
            #print("false")
            break
        #else:
            #print("true")

def draw_rectangle(column,row,length,height,p,color):
    i=0
    while(i<height):
        draw_row(column,row+i,length,p,color)
        i=i+1
        if(math.floor(turtle.ycor())<=-9*p):
            #print(str(10*p) + " " + str(turtle.ycor()))
            #print("false")
            break
        #else:
            #print("true")

def get_random_hex():
    x = random.randint(0,15)
    if x == 0:
        return "0"
    else:
        return hex(x).lstrip("0x")

def get_hex_color():
    i=0
    hexcolor = "#"
    while(i<6):
        hexcolor += get_random_hex()
        i+=1
    return hexcolor

def draw_random_rectangle(p):
    draw_rectangle(random.randint(0,19),random.randint(0,19),random.randint(0,19),random.randint(0,19),p,get_hex_color())

def draw_list(p,list):
    i=0
    if len(list) == 400:
        j=0
        i=0
        while j < 20:
            while i < 20:
                if list[j*10+i] != 0:
                    move(i,j,p)
                    draw_pixel(p,list[j*10+i])
                    i+=1
                j+=1


def build_list():
    i = 0
                
    




def main():
    pixel_size = 30
    pixel_color = "gold"
    draw_grid(pixel_size)
    # draw_pixel(pixel_size,pixel_color)
    # move(3,8,pixel_size)
    # draw_row(15,3,8,pixel_size,pixel_color)
    # draw_rectangle(19,19,10,7,pixel_size,pixel_color)
    #input("Type to end program: ")
    # draw_random_rectangle(pixel_size)

main()