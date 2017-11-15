from flask import Flask
from flask import redirect, url_for, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/haha/<username>')
def haha(username):
    return "Hello {}".format(username)


@app.before_request
def before_request():
    username = request.args.get('username')
    if username is not None:
        print(username)
        return redirect(url_for('haha', username=username))


if __name__ == '__main__':
    app.run()


# http://localhost:5000?username=apktool
# It's Ok, The hooks function will rediret above url to follow url
# http://localhost:5000/haha/apktool
