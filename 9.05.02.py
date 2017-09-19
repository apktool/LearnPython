# flask basic knowlege


from flask import Flask, redirect, url_for, request, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Hello world</h1>'


@app.route('/user/<username>')
def name(username):
    return '<h1> {0}</h1>'.format(username)


@app.route('/user/age/<int:age>')
def age(age):
    return '<h1>age %d </h1>' % age


@app.route('/about')
def about():
    return '<h1>ABOUT</h1>'


@app.route('/register', methods=['POST', 'GET'])
def register():
    return redirect(url_for('index'))


def do_the_login():
    return '<h1>Login Sucess</h1>'


def show_the_login_form():
    value = request.args.get('next')
    return '<h2>show login form sucess, value achieved is <h2>' + value


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        msg = do_the_login()
    else:
        msg = show_the_login_form()
    return msg


@app.errorhandler(404)
def page_not_found(error):
    return '<h1>Page Not Found', 404


with app.test_request_context():
    print(url_for('index'))
    print(url_for('name', username='li'))
    print(url_for('about', next='abc'))


@app.route('/hello')
@app.route('/hello/<username>')
def hello(username=None):
    return render_template('hello.html', name=username)
