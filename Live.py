from GuessGame import play_gg
from CurrencyRouletteGame import play_crg
from MemoryGame import play_mg


def welcome(name):  # greeting function
    return ((f"Hello {name} and welcome to the World of Games (WoG).\n"
             "Here you can find many cool games to play."), name)


def load_game(name):  # Function to choose a game and difficulty level
    # in the future if other options should be added need to add only
    # on lists and on the input text for the new options
    list_game_choice = ["1", "2", "3"]
    list_game_difficulty = ["1", "2", "3", "4", "5"]
    game_choice = input("""Please choose a game to play:
          1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
          2. Guess Game - guess a number and see if you chose like the computer
          3. Currency Roulette - try and guess the value of a random amount of USD in ILS)\n""")
    while game_choice.isdigit() is False or game_choice not in list_game_choice:  # Check that the input is valid
        # number and on the desired range for Game decision
        game_choice = input(f"Please enter a number between 1 and {len(list_game_choice)}: \n")
    else:
        game_difficulty = (input(f"Please choose game difficulty from 1 to {len(list_game_difficulty)}: \n"))
        while game_difficulty.isdigit() is False or game_difficulty not in list_game_difficulty:  # Check that the
            # input is valid number and on the desired range for difficulty decision
            game_difficulty = input(f"Please enter a number between 1 and {len(list_game_difficulty)}: \n")
        # Call the game of choice
    if int(game_choice) == 1:
        play_mg(int(game_difficulty), name)
    elif int(game_choice) == 2:
        play_gg(int(game_difficulty), name)
    else:
        play_crg(int(game_difficulty), name)
