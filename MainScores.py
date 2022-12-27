from flask import Flask, render_template
import json
from Utils import scores_file_name
from Utils import bad_return_code
import os
from operator import attrgetter

if not os.path.exists(scores_file_name):
    app = Flask(__name__)

    @app.route('/')  # landing page with links to content and register pages
    def links():
        return render_template("scoreerror.html", badcode=bad_return_code)


    if __name__ == '__main__':
        app.run('0.0.0.0', debug=True, port=30000)
else:
    fh = open(scores_file_name, "r")
    actual_score_str = fh.read()
    actual_score = json.loads(actual_score_str)
    app = Flask(__name__)


    @app.route('/')  # landing page with links to content and register pages
    def links():
        return render_template("score.html", score=actual_score)
    if __name__ == '__main__':
        app.run('0.0.0.0', debug=True, port=30000)
