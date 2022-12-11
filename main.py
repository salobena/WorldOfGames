from Live import load_game, welcome
import os

os.system('clear')
name = welcome(input("Hey there! what is your name?\n "))[1]
load_game(name)
