'''
    MasterMind Game Driver
    CS5001 Final Project
    Thank you Mr. Bagley and TAs!
'''
import turtle
import datetime
from threading import Timer
from Point import Point
from Marble import Marble
from Row import Row
from secret_code import *
from graphics import *
from button_helper import *
from leaderboard import *


def check(point, secret_code, chosen_colors, center):
    '''
    check answer if check button is clicked
    if so, return True and checked result
    otherwise, return False and None
    '''
    if in_or_not(point.x, point.y, [center, 'circle', 30]):
        result = comparison(secret_code, chosen_colors)
        return (True, result)
    else:
        return (False, None)  

def timer(f, time):
    '''execute f in time (float or int) seconds'''
    mytimer = Timer(time, f)
    mytimer.start()

def mastermind_game():
    '''the main game function'''
    # initialize the game board
    mastermind, username = initialize_gameboard()

    # draw the display circles
    gameboard = initialize_display_circles()

    # draw the user panel circles
    user_panel = Row(initialize_user_panel())

    # initialize the buttons
    checkbutton = Point(0, -280)
    xbutton = Point(80, -280)
    quitbutton = Point(280, -280)

    initialize_buttons(mastermind, checkbutton, xbutton, quitbutton)

    # initialize the pointer
    pointer = set_image(mastermind, "pointer_cropped.gif", Point(-350, 340))

    # set global message display time
    message_time = 3.0

    # read record
    leaderboard_writer = turtle.Turtle()
    try:
        screen_writer(leaderboard_writer,
                      read("leaderboard.txt"))
    except FileNotFoundError:
        # show the error message
        error_message = set_image(mastermind, "leaderboard_error.gif")

        # hide the message after given time
        timer(error_message.ht, message_time)    
        # leaderboard shows error message
        write("leaderboard.txt", '')
    # initialize secret code
    secret_code = generator()

    chosen_colors = []
    trial = []

    def restart():
        '''
        restart the game
        including steps below:
        regenerate secret code
        reset display
        reset user panel
        reset trial time
        reset pointer
        '''
        # get new secret code
        secret_code.clear()
        new_secret = generator()
        for each in new_secret:
            secret_code.append(each)

        # reset pointer
        pointer.goto(-350, 340)

        # reset the display
        for each in gameboard[0]:
            row = Row(each)
            row.reset_panel(["white", "white",
                             "white", "white"])
        for each in gameboard[1]:
            row = Row(each)
            row.reset_panel(["white", "white",
                             "white", "white"])
        user_panel.reset_panel()

        # reset others
        chosen_colors.clear()
        trial.clear()

    def user_panel_clicker(point):
        '''
        makes the user panel clickable
        changes button color and remembers chosen colors
        only effective if chosen colors are less than 4
        and the button not already chosen
        takes a Point object representing the click
        return True if it's an effective click
        '''
        number_of_white = 0
        # check how many have been chosen
        for each in user_panel.marbles:
            if each.get_color() == "white":
                number_of_white += 1
        for index, value in enumerate(user_panel.marbles):    
            if number_of_white < 4: # make sure only four chosen
                if value.clicked_in_region(point.x, point.y) and \
                   value.get_color() != "white":
                    chosen_colors.append(value.get_color())
                    user_panel.marbles[index].set_color("white")
                    value.erase()
                    value.draw()
                    return True

    def button_functions(x, y):
        '''uses input cordination to trigger game functions'''
        try: # error logging inside the click function
            display_row = Row(gameboard[0][len(trial)])

            click_point = Point(x, y)

            if user_panel_clicker(click_point): # if clicked a valid color
                # changing the display
                changing = display_row.marbles[len(chosen_colors) - 1]
                changing.change_color(chosen_colors[-1])

            # check or cancel the choice made
            checked = check(click_point,
                  secret_code, chosen_colors, checkbutton)
            canceled = in_or_not(click_point.x, click_point.y,
                                 [xbutton, 'circle', 30])
            quit_status = in_or_not(click_point.x, click_point.y,
                                 [quitbutton, 'rectangle', 100, 56])
            if checked[0]:
                # display the result
                result_display(checked[1], gameboard, len(trial))

                # rest user panel and chosen colors list
                user_panel.mass_erase()
                user_panel.reset_panel()
                chosen_colors.clear()

                # trial times plus 1
                trial.append('')

                # pointer down a row
                pointer_mover(pointer, len(trial))

                # check
                if checked[1][0] == 4: # if won
                    winner = set_image(mastermind, "winner.gif")
                    record = [username, str(len(trial))]
                    leaderboard_new = leaderboard_output(
                        leaderboard_requencer(
                            leader_board_reader(read('leaderboard.txt')), record))
                    write("leaderboard.txt", leaderboard_new)

                    timer(winner.ht, message_time)
                    restart()

                    # reprint the leaderboard
                    leaderboard_writer.clear()
                    screen_writer(leaderboard_writer, leaderboard_new)

                else:
                    if len(trial) == 10:
                        lose = set_image(mastermind, "lose.gif")

                        timer(lose.ht, message_time)
                        restart()

            elif canceled:
                user_panel.reset_panel()
                display_row.reset_panel(["white", "white",
                                         "white", "white"])
                chosen_colors.clear()

            elif quit_status: # if quit button clicked
                # first send message
                set_image(mastermind, "quitmsg.gif")
                # 3s to quit
                timer(mastermind.bye, message_time)

        except Exception as error_message:
            error_time = datetime.datetime.now()
            with open('mastermind_errors.err', 'a') as file:
                log = f"Got {type(error_message)} at {str(error_time)}, \
    the message is \"{error_message}\""
                file.write(log + "\n")

    mastermind.onclick(button_functions)
    mastermind.mainloop()

def main():
    try:
        mastermind_game()
    # error logging
    except Exception as error_message:
        error_time = datetime.datetime.now()
        with open('mastermind_errors.err', 'a') as file:
            log = f"Got {type(error_message)} at {str(error_time)}, \
the message is \"{error_message}\""
            file.write(log + "\n")

if __name__ == "__main__":
    main()
