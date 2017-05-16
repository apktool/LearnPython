from flask import Flask, url_for, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1> hello world </h1>'


@app.route('/user')
def profile():
    tmp = 2
    if tmp is 1:
        return redirect(url_for('index'))
    return '<h1> UserProfile </h1>'


if __name__ == '__main__':
    app.run()
