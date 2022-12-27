# import requests
# import json
import random
import os
from currency_converter import CurrencyConverter
from Score import add_score
from Utils import screen_cleaner


def guess_game_greeting_crg(game_difficulty, name):
    print(input(f"""Hey {name} Welcome to the Currency Roulette Game!
    In this game you will need to calculate the amount of Shekels according
    to a specific random amount of dollars depending on the difficulty level 
    you will need to be more sharp """))
    return game_difficulty, name


def get_money_interval(game_difficulty):
    dollar_amount = random.randint(0, 101)
    print(dollar_amount)
    # using API
    # url = "https://currency-converter5.p.rapidapi.com/currency/convert"
    # querystring = {"format": "json", "from": "USD", "to": "ILS", "amount": dollar_amount}
    # headers = {
    #     "X-RapidAPI-Key": "39d97a81f3msh8f4135d66dba709p1e7c1fjsn781bebd2a3d4",
    #     "X-RapidAPI-Host": "currency-converter5.p.rapidapi.com"
    # }
    # response = requests.request("GET", url, headers=headers, params=querystring)
    # listall = json.loads(response.text)
    # shekel_cur = listall['rates']['ILS']['rate_for_amount']
    # test1 = float(shekel_cur)
    # shekel_cur = round(test1)

    # using library:
    c = CurrencyConverter()
    shekel_cur = c.convert(dollar_amount, 'USD', 'ILS')
    money_range = (shekel_cur - (5 - game_difficulty), shekel_cur + (5 - game_difficulty))
    return money_range, dollar_amount, shekel_cur


def get_guess_from_user(dollar_amount):
    shekel_amount = 'a'
    while shekel_amount.isdigit() is False:
        shekel_amount = input(f"What you think is the right amount of shekel for ${dollar_amount}? \n")
    return int(shekel_amount)


def play_crg(game_difficulty, name):
    screen_cleaner()
    guess_game_greeting_crg(game_difficulty, name)
    values = get_money_interval(game_difficulty)
    money_range = values[0]
    dollar_amount = values[1]
    guess = get_guess_from_user(dollar_amount)
    if money_range[0] < guess < money_range[1]:
        print(" you Won!!" + " This is the range: " + str(money_range) + " and this is your guess: " + str(guess))
        result = True
        add_score(game_difficulty, name, result)
    else:
        print(" you lose" + " This is the range: " + str(money_range) + " and this is your guess: " + str(guess))
        result = False
        add_score(game_difficulty, name, result)
    play_again = input("Would you like to play again? (y for yes): \n ")
    if play_again.lower() == 'y':
        play_crg(game_difficulty, name)
