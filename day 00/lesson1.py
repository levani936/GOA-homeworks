from turtle import *


#we want to paint a house

#step 1:  draw a square
width(7)
color("purple")
forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door

forward(70)
begin_fill()
color("yellow")
left(90)
forward(120)    #height of the door
right(90)
forward(60)
right(90)
forward(120)
end_fill()
penup()
goto(200, 200)
pendown()

color("red")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()
color("purple")
left(30)
forward(80)
color("brown")
left(90)
begin_fill()
forward(65)
right(90)
forward(65)
right(90)
forward(65)
end_fill()
color("purple")
left(90)
forward(55)
left(90)
forward(200)
left(90)
forward(55)
left(90)
color("brown")
begin_fill()
forward(65)
right(90)
forward(65)
right(90)
forward(65)
end_fill()







exitonclick()