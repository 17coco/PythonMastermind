'''
    functions for the secret code generation and comparison
'''
import random

def generator():
    '''generates the secret code'''
    colors = ["red", "blue", "green", "yellow", "purple", "black"]
    secret_code = []
    while len(secret_code) < 4:
        index = random.randint(0, len(colors) - 1)
        secret_code.append(colors.pop(index))

    return secret_code

def comparison(secret_code, guess):
    '''
    compares two lists or tuples
    returns a tuple of bulls and cows
    bulls is the number of elements identical
    in both position and value
    cows is the number of indentical elements
    in different positions
    '''
    cows = 0
    bulls = 0
    
    for index, value in enumerate(secret_code):
        for number, color in enumerate(guess):
            # completely right
            if index == number and value == color:
                bulls += 1
            # only color is right
            elif index != number and value == color:
                cows += 1
    return (bulls, cows)
