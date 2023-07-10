# Joshua Soto
# 1553869

import math

paint_colors = {
    'red': 35,
    'blue': 25,
    'green': 23
}

wall_height = int(input('Enter wall height (feet):\n'))
wall_width = int(input('Enter wall width (feet):\n'))
wall_area = (wall_height * wall_width)
print('Wall area:', wall_area, 'square feet')

area_per_gallon = float(1 / 350)
paint_needed = (wall_area * area_per_gallon)

print('Paint needed: ' + str('{:.2f}'.format(paint_needed)) + ' gallons')

cans_needed = math.ceil(paint_needed)
print('Cans needed:', cans_needed, 'can(s)\n')

user_colors = input('Choose a color to paint the wall:\n')
paint_price = paint_colors[user_colors]
total_price = int(paint_price) * cans_needed

print('Cost of purchasing %s paint: $%d' % (user_colors, total_price))
