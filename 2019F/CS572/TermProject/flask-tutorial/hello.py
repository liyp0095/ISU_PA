from flask import Flask
from flask import render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/')
@app.route('/board')
def board():
    return render_template('board.html', title='Home')


if __name__ == "__main__":
    app.run()
