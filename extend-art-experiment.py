#Square Rainbow
import turtle
shelly = turtle.Turtle()
shelly.shape('turtle')


colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow']

for i in range(6):
    shelly.color(colors[i])
    for n in range(4):
        shelly.forward(20)
        shelly.left(90)
    shelly.penup()
    shelly.forward(30)
    shelly.pendown()

print(i)

shelly.reset()
# make face cirlce 
shelly.begin_fill()
shelly.color('green')
shelly.circle(100)
shelly.end_fill()

#make one eye
shelly.penup()
shelly.goto(-30,100)
shelly.pendown()
shelly.begin_fill()
shelly.color('white')
shelly.circle(30)
shelly.end_fill()
shelly.begin_fill()
shelly.color('black')
shelly.circle(20)
shelly.end_fill()

#make second eye
shelly.penup()
shelly.goto(30,100)
shelly.pendown()
shelly.begin_fill()
shelly.color('white')
shelly.circle(30)
shelly.end_fill()
shelly.begin_fill()
shelly.color('black')
shelly.circle(20)
shelly.end_fill()

#make square mouth
shelly.penup()
shelly.goto(-10,15)
shelly.pendown()
shelly.begin_fill()
for i in range(4):
 shelly.forward(20)
 shelly.left(90)
shelly.end_fill()
print(i)


