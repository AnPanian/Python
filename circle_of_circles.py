#import turtle
import turtle
shelly = turtle.Turtle()
shelly.shape('turtle')

colors = ['red', 'yellow', 'blue', 'orange', 'green', 'white']
#6 repeating circles
for i in range(36):
    shelly.penup()
    shelly.forward(200)
    
    
    for n in range (5):
      shelly.pendown()
      shelly.color(colors[n]) 
      shelly.circle(5)
      shelly.penup()
      shelly.backward(20)

    shelly.goto(0,0)
    shelly.right(10)




