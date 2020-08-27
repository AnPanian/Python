import turtle
shelly = turtle.Turtle()
shelly.shape('turtle')

for i in range (4):
 shelly.forward(100)
 shelly.left(90)

print (i)

shelly.begin_fill()
shelly.color('red')
for i in range (4):
 shelly.forward(100)
 shelly.left(90)
 
print (i)
shelly.end_fill()

shelly.reset()

for i in range (50):
 for n in range (4):
  shelly.forward(100)
  shelly.left(90)
 shelly.right(35)

 print (i)
 
  



