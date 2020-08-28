# Make a Hexagon

import turtle
shelly = turtle.Turtle()
shelly.shape('turtle')

colors = ['red', 'orange', 'yellow', 'green', 'blue', 'red']
turtle.bgcolor('black')

for n in range(36):
    for i in range(6):
      shelly.color(colors[i])
      shelly.forward(100)
      shelly.left(60)
    shelly.right(10)
print(n)

shelly.penup()
shelly.color('white')

for b in range (36):
    shelly.forward(220)
    shelly.pendown()
    shelly.circle(7)
    shelly.penup()
    shelly.backward(220)
    shelly.right(10)
shelly.hideturtle()
print(b)
