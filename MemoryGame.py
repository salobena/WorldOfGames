import random
import os
import time


def guess_game_greeting_mg(game_difficulty, name):
    print(input(f"""Hey {name} Welcome to the Memory Game!
    In this game you will need to remember a list of numbers.
    The amount of numbers will be the number you choose on the difficulty level
    The numbers will appear for less then a second press ENTER when ready \n"""))
    return game_difficulty, name


def generate_sequence(game_difficulty):
    list_random = []
    for i in range(1, game_difficulty + 1):
        list_random.append(random.choice(range(1, 101)))
    return list_random


def get_list_from_user(game_difficulty):
    list_user = []
    number = 'a'
    for i in range(1, game_difficulty + 1):
        while number.isdigit() is False:
            number = (input("Please enter one of the  numbers : \n"))
        else:
            list_user.append(int(number))
    return list_user


def is_list_equal(list_random, list_user):
    list_random.sort()
    list_user.sort()
    if list_random == list_user:
        result = True
    else:
        result = False
    return result


def play_mg(game_difficulty, name):
    os.system('clear')
    guess_game_greeting_mg(game_difficulty, name)
    list_random = generate_sequence(game_difficulty)
    print(list_random)
    time.sleep(0.7)
    os.system('clear')
    list_user = get_list_from_user(game_difficulty)
    result = is_list_equal(list_random, list_user)
    if result is True:
        print(f"Congratulations you WON ! \n")
    else:
        print(f"Sorry you lost... the right numbers were {list_random} \n")
    play_again = input("Would you like to play again? (y for yes): \n ")
    if play_again.lower() == 'y':
        play_mg(game_difficulty, name)

    # print(list_random, list_user)
