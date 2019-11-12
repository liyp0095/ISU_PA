from flask import Flask
from flask import request, jsonify
from flask import render_template

app = Flask(__name__, template_folder='templates')


@app.route('/')
def hello():
    return 'Hello, World!'


@app.route('/')
@app.route('/board')
def board():
    return render_template('board.html', title='Home')


@app.route('/test')
def test():
    return render_template('t1.html', title='Home')


# ajax，Get方式与js交互(非表单）
@app.route('/_add_numbers')
def add_numbers():
    """Add two numbers server side, ridiculous but well..."""
    a = request.args.get('a', 0, type=int)
    b = request.args.get('b', 0, type=int)
    # log.info(a)
    # log.info(b)
    return jsonify(result=a + b)


if __name__ == "__main__":
    app.run()
