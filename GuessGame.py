import random
import os


def guess_game_greeting_gg(game_difficulty, name):
    print(f"""Hey {name} Welcome to the Guess Game!
    In this game you will need to Guess a number between 1 and the
    difficulty level number you choose previously:""")
    return game_difficulty, name


def generate_number(game_difficulty):
    secret_number = random.randint(1, game_difficulty)
    return secret_number


def get_guess_from_user(game_difficulty):
    choose_number = input(f"Choose a number between 1 and the {game_difficulty}: \n")
    while choose_number.isdigit() is False or int(choose_number) < 1 or int(choose_number) > game_difficulty:
        choose_number = input(f"Choose a number between 1 and the {game_difficulty}: \n")
    else:
        return int(choose_number)


def compare_results(secret_number, choose_number):
    same_number = 0
    # print(choose_number, secret_number)
    if secret_number == choose_number:
        same_number = 1
    else:
        same_number = 0
    return same_number
    # print(same_number)


def play_gg(game_difficulty, name):
    os.system('clear')
    guess_game_greeting_gg(game_difficulty, name)
    secret_number = generate_number(game_difficulty)
    choose_number = get_guess_from_user(game_difficulty)
    result = compare_results(secret_number, choose_number)
    if result == 1:
        print(f"Congratulations you WON ! \n")
    else:
        print(f"Sorry you lost... the right numbers was {secret_number} \n")
    play_again = input("Would you like to play again? (y for yes): \n ")
    if play_again.lower() == 'y':
        play_gg(game_difficulty, name)
