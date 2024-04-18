# PythonMastermind
A mastermind game with turtle-based GUI.
## Design Notes
The Process

First，I wrote a text version of the game. The function that generates the secret code and the other one that tests for numbers of bulls and cows were actually used in the main program later.

Then, I worked on drawing out the user interface with turtle. It is composed of the frames, the marbles, and other buttons. I saved all the marble objects into lists for future recalls. The button images were set by using turtle register_shape() method. I found a pointer gif from internet and reshape it and quit button gif to fit better in the interface.

After that, what I did was to make all buttons do their things. I build a series of functions around the onclick() method. 

My button_functions() receives x, y coordination from onclick() and pass it to other functions. Every time the use click on the screen, the game will check if it's in the area of the buttons, using Pythagorean theorem for circles and simple calculation for rectangles. Marbles use their built in method and other buttons use in_or_not(). To use local value x, y, I implemented some nested functions.

user_panel_clicker() is dedicated to the marbles on the lower left screen, changing a marble's color when it's clicked, remember it by appending the color to chosen_colors list. Only 4 can be chosen and a chosen color cannot be chosen again. Chosen_colors will later be passed to change the display row marble color.

If the user presses the check button, the game will check answers by comparing color strings and their positions. After checking, the game sees if we get 4 bulls or reach 10 times, if so it shows messages and restart, if not it will just show results will result_display() to show results and go to next attempt. result_display() decides which row it's on by trial times and make the same number of bulls of marbles black, then start from the first white marble after that to make marbles to show number of cows.

The cancel button will clean current choices.

Also, I created a new class named Row to deal with a group of marbles using its method. This makes it easier to reset a bunch of marbles every time it's canceled or reset.

To make one game exactly 10 attempts and track the current position. I used a variable called trial. Trial starts as an empty list, is appended an empty string every attempt, and is clear()ed after winning or losing. After winning or losing, all things will reset by calling restart(). Somehow the reset takes a bit long.

For showing win, lose, and file error messages for certain time, I used Timer from threading module. After a given time which is set to be 3 seconds, all these messages will disappear and next steps will be carried out. For the quit button, the program will quit after showing the quit message for 3 seconds.

Next, I tried to implement the leaderboard feature. I decided to save 5 best scores to make it look more similar to an actual leaderboard. If there's no leaderboard file, the game will show an error message for 3 seconds and create a file after winning. Other than reading and writing files, the leaderboard functions can sort all saved scores with a new record. All records after 5th will not be saved. The new leaderboard will be printed in turtle immediately after the game resets itself following winning.

Last, I figured out how to handle the errors and get error messages and error time. I imported datetime module and used datetime.now() to  get system date and time. I used except Exception as error_message to get the exact error message.

I have graphics.py to hold all my functions dedicated to build the user interface; all the functions about leaderboard is in leaderboard.py; my Row class is in Row.py; button_helper.py is functions that's written for buttons.
