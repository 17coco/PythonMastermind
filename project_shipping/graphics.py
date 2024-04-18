'''
    graphics related functions
'''
import turtle
from Point import Point
from Marble import Marble

def pointer_mover(pointer_turtle, current_row):
    '''
    move the pointer to current row
    '''
    if current_row < 10:
        current_y = pointer_turtle.ycor()
        pointer_turtle.sety(current_y - 50)

def initialize_gameboard():
    '''initialize the game board'''
    mastermind = turtle.Screen()
    mastermind.delay(0)
    username = mastermind.textinput("CS5001 MasterMind", "What's your name?")
    if username is None:
        username = "Anonymous"
    mastermind.setup(800, 800, None, None)
    mastermind.title("MasterMind CS5001")
    # initialize the rectangles
    draw_a_rectangle(400, 600, Point(-390, 390), "black")
    draw_a_rectangle(775, 160, Point(-390, -225), "black")
    draw_a_rectangle(360, 600, Point(20, 390), "blue")
    return (mastermind, username)

def initialize_buttons(screen, checkbutton, xbutton, quitbutton):
    '''initializes check/cancel/quit buttons'''

    set_image(screen, "checkbutton.gif", checkbutton)
    set_image(screen, "xbutton.gif", xbutton)
    set_image(screen, "quit_cropped.gif", quitbutton)

def screen_writer(myturtle, content):
    '''write given content on screen'''
    pen = myturtle
    pen.ht()
    pen.pencolor("blue")
    pen.up()
    y = 350
    pen.setpos(50, y)
    content = content.split('\n')
    for each in content:
        pen.write(each, font=('Arial', 20, 'normal'))
        y -= 20
        pen.setpos(50, y)
    y = 280
    pen.setpos(50, y)

def result_display(bulls_and_cows, gameboard, current_row):
    '''
    parameters:
    a bulls and cows tuple
    gameboard (list of all Marble objects in the display)
    current row (integer indicating which row is being worked)
    change the result display status
    '''
    bulls = bulls_and_cows[0]
    cows = bulls_and_cows[1]
    # get the list of the four Marbles of the changing row
    changing = gameboard[1][current_row]

    # display the bulls
    for i in range(0, bulls):
        changing[i].change_color("black")

    # display the cows
    for i in range(bulls, bulls + cows):
        changing[i].change_color("red")

def set_image(screen, filename, position=Point(0, 0)):
    '''set position for a image'''
    screen.register_shape(filename)
    image_turtle = turtle.Turtle(filename, visible=False)

    image_turtle.up()
    image_turtle.setx(position.x)
    image_turtle.sety(position.y)
    image_turtle.showturtle()

    return image_turtle

def draw_a_rectangle(width, height, position, color):
    '''
    draw a square and the center of the square is (x, y)
    prarmeter:
    myTurtle
    the length of each side
    '''

    pen = turtle.Turtle()
    pen.color(color)
    pen.up()
    pen.hideturtle()
    pen.setx(position.x)
    pen.sety(position.y)
    pen.pensize(6)
    pen.speed(0)
    pen.setheading(0)

    pen.down()
    pen.forward(width)
    pen.right(90)
    pen.forward(height)
    pen.right(90)
    pen.forward(width)
    pen.right(90)
    pen.forward(height)

def initialize_display_circles():
    '''initialize display circles'''
    guess_circles = []
    bull_cow_reminders = []
    big_position = Point(-300, 320)
    small_position = Point(-110, 340)

    for i in range(0, 10):
        list_of_a_row = []
        dot_list_of_a_row = []

        # draw the big color display circles
        for k in range(0, 4):
            circle = Marble(big_position, "White")
            circle.draw()
            # build list of each row
            list_of_a_row.append(circle)
            big_position = Point(big_position.x + 40, big_position.y)
        # put lists of each row into nested list
        guess_circles.append(list_of_a_row)

        # draw the dots for bulls and cows
        for n in range(0,2):
            for l in range(0,2):
                dot = Marble(small_position, "White", 4)
                dot.draw()
                # build list of each row
                dot_list_of_a_row.append(dot)
                small_position = Point(small_position.x + 12, small_position.y)
            small_position = Point(-110, small_position.y - 20)

        # put lists of each row into nested list
        bull_cow_reminders.append(dot_list_of_a_row)
        big_position = Point(-300, big_position.y - 50)
        small_position = Point(-110, big_position.y + 20)

    return (guess_circles, bull_cow_reminders)

def initialize_user_panel():
    '''initialize the user panel circles'''
    colors = ["red", "blue", "green", "yellow", "purple", "black"]
    user_panel = []
    position = Point(-280, -300)
    for each in colors:
        circle = Marble(position, each)
        circle.draw()
        user_panel.append(circle)
        position = Point(position.x + 40, position.y)

    return user_panel
