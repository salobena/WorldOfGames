import os
from Utils import scores_file_name
import json


def add_score(game_difficulty, name, result):
    # verify the scores received and create variables to feed file
    points_of_winning = (game_difficulty * 3) + 5
    if result:
        win = 1
        lost = 0
    else:
        win = 0
        lost = 1
        points_of_winning = 0
    if not os.path.exists(scores_file_name):
        fh = open(scores_file_name, "w+")
        score = {0: {'name': name.lower(), 'point': points_of_winning, 'win': win, 'lost': lost}}
        print(type(score))
        fh.write(json.dumps(score))
        exit()
    else:
        fh = open(scores_file_name, "r")
        actual_score_str = fh.read()
        actual_score = json.loads(actual_score_str)
        # print(type(actual_score))
        number_of_lines = (len(actual_score.values()))
        # print(number_of_lines)
        if actual_score != "":
            for key, value in actual_score.items():
                if str(value).__contains__(name.lower()):
                    name_exists = key
                    # print(name_exists)
                    break
                else:
                    name_exists = ""
    if number_of_lines < 3 or name_exists != "":
        pass
    else:
        mn_points = min((points['point']) for points in actual_score.values())
        for key, value in actual_score.items():
            if str(value).__contains__(str(mn_points)):
                name_to_pop = key
                actual_score.pop(name_to_pop)
                break

    if name_exists != "":
        current_point = actual_score[name_exists]['point']
        current_wins = actual_score[name_exists]['win']
        current_losses = actual_score[name_exists]['lost']
        print(current_point)
        actual_score[name_exists]['point'] = current_point + points_of_winning
        actual_score[name_exists]['win'] = current_wins + win
        actual_score[name_exists]['lost'] = current_losses + lost
        fh = open(scores_file_name, "w+")
        fh.write(json.dumps(actual_score))
    else:
        score = {number_of_lines: {'name': name.lower(), 'point': points_of_winning, 'win': win, 'lost': lost}}
        actual_score.update(score)
        fh = open(scores_file_name, "w+")
        fh.write(json.dumps(actual_score))
    print(actual_score)
    fh.close()



add_score(1, 'salo', True)
