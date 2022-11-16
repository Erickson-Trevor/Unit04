import turtle

def initalize(p):
    turtle.speed(0)
    turtle.pencolor("black")
    turtle.penup()
    turtle.goto(-10*p,10*p)

def draw_pixel(p,c):
    turtle.pendown()
    turtle.fillcolor(c)
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

def move(row,column,p):
    turtle.goto((column-10)*p,(row+10)*p)


def main():
    pixel_size = 30
    pixel_color = "red"
    draw_grid(pixel_size)
    # draw_pixel(pixel_size,pixel_color)
    move(3,8,pixel_size)
    input("Type to end program: ")

main()
