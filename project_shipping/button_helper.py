'''click functions'''
from Point import Point

def in_or_not(click_x, click_y, button):
    '''
    checks if a position is inside a shape
    button is a list that
    includes center, shape, radius for a circle
    or center, shape, width, length for a rectangle
    '''
    center = button[0]
    shape = button[1]

    click = Point(click_x, click_y)
    if shape == 'circle':
        radius = button[2]
        if click.delta_x(center) ** 2 + \
            click.delta_y(center) ** 2 < radius ** 2:
            return True

        return False

    if shape == 'rectangle':
        width = button[2]
        length = button[3]
        if click.delta_x(center) < width * 0.5 and \
            click.delta_y(center) < length * 0.5:
            return True

        return False
