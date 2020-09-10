import turtle
shelly = turtle.Turtle() 
shelly.shape('turtle')

#background
turtle.bgcolor('blue')

#house
shelly.begin_fill()
shelly.color('gray')

for i in range(4):
  shelly.forward(100)
  shelly.left(90)

shelly.end_fill()

#roof
shelly.penup()
shelly.goto(-20, 100)
shelly.pendown()
shelly.begin_fill()
shelly.color('red')
shelly.left(60)
shelly.forward(140)
 
for n in range(2):
    shelly.right(120)
    shelly.forward(140)

shelly.end_fill()

#window
shelly.penup()
shelly.goto(25,80)
shelly.pendown()
shelly.begin_fill()
shelly.color('yellow')

for i in range(4):
    shelly.forward(20)
    shelly.left(90)
shelly.end_fill()









