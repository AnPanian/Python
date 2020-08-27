import turtle
shelly = turtle.Turtle()
shelly.shape('turtle')

colors = ['red', 'orange', 'yellow' 'green', 'blue', 'purple']

for i in range(6):
    shelly.color(colors[i])
    shelly.forward(50)
    print(colors[i])



