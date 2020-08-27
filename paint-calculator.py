# Calculate how much paint to purchase

#height of the room
height = input('What is the height of your room in feet?: ')

height = int(height)

#width of the room 
width = input('What is the width of your room in feet?: ')

width = int(width)

#length of the room
length = input('What is the length of your room in feet?: ')

length = int(length)

#windows
windows = input('How many windows are in this room?: ')

windows = int(windows)

#doors 
doors = input('How many doors are in this room?: ')

doors = int(doors)

#set no paint area
no_paint = (20 * doors) + (15 * windows)

#Set total wall area
wall_area = (2 * length * height)+ (2 * width * height)

# Remove no paint area
paint_area = wall_area - no_paint

print('Your paintable wall area is ', paint_area, 'feet.')

#Number of gallons needed
gallons = paint_area / 350

gallons = round(gallons)

#Number of gallons needed
print('You will need ', gallons, 'gallons of paint to complete this project.')



