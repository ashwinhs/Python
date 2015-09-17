import turtle
import time

def draw(some_turtle, sides, angle, sideLength):
    some_turtle.speed(200)
    if sides == 0:
        some_turtle.circle(sideLength)
    elif sides == -1:
        some_turtle.right(90)
        some_turtle.forward(300)
    else:
        for i in range(sides):
            some_turtle.forward(sideLength)
            some_turtle.right(angle)

def draw_shape(dturtle, shape):
    if shape.lower() == 'square':
        draw(dturtle, 4, 90, 100)
    elif shape.lower() == 'triangle':
        draw(dturtle, 3, 120, 100)
    elif shape.lower() == 'circle':
        draw(dturtle, 0, 10, 100)
    elif shape.lower() == 'rhombus':
        for i in (1,2):
            draw(dturtle, 1, 60, 100)
            draw(dturtle, 1, 120, 100)
    elif shape.lower() == 'line':
        draw(dturtle, -1, 0, 0)
    elif shape.lower() == 'flower':
        draw(tur, 0, 0, 50)
        draw(tur, 0, 0, 100)
        draw(tur, 0, 0, 200)
        draw(tur, 0, 0, 10)

def draw_leaf(turtle):
    base = turtle.pos()
    turtle.circle(70,75)
    turtle.goto(base)
    turtle.circle(-70,75)
    turtle.goto(base)

def get_window():
    w = turtle.Screen()
    w.bgcolor("Red")
    return w

def get_turtle():
    t = turtle.Turtle()
    t.color("Yellow")
    t.shape("turtle")
    return t

def clear_turtle(t, shape=None):
    t.clear()
    t.pu()
    t.setpos(0,150)
    if shape == "flower":
        t.setpos(0,0)
    t.pd()
    
 
shapeList = ["square", "triangle", "circle", "rhombus", "flower"]

window = get_window()
tur = get_turtle()


for shape in shapeList:
    clear_turtle(tur, shape)
    for i in range(1,37):
        draw_shape(tur, shape)
        tur.right(10)
    if shape == "rhombus":
        draw_shape(tur, "line")

    time.sleep(5)



window.exitonclick()