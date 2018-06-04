from flask import Flask
from flask import jsonify
from flask import request
from flask import render_template
from prefix_game import prefix_game

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('attempt3.html')


@app.route('/draw/<text>/', methods=['GET', 'POST'])
def newpresuff(text):
    game = prefix_game()
    result = game.draw_prefixes()
    print(jsonify(result))
    return jsonify(result)


@app.route('/sound/<text>', methods=['GET','POST'])
def sound(text):
    return '/static/wrong.mp3'


@app.route('/iscorrect/<text>/', methods=['GET', 'POST'])
def iscorrect(text):
    game = prefix_game()
    if (game.is_correct(text)):
        return "/static/right.mp3"
    else:
        return "/static/wrong.mp3"


@app.route('/reset/', methods=['GET', 'POST'])
def reset():
    return ('', 204)


if __name__ == '__main__':
    app.run()
