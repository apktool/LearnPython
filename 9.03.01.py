# flask | cookie | add,delete,modify,get


from flask import Flask, request
from flask import request, make_response

app = Flask(__name__)

@app.route('/')
def index():
    return '<h1>Hello World</h1>'

@app.route('/setcookie')
def setcookie():
    resp = make_response('<h1>Cookie is set Success<h1>')
    resp.set_cookie('username', 'Apktool')
    return resp

@app.route('/getcookie')
def getcookie():
    username = request.cookies.get('username')
    return '<h1> Hello {} </h1>'.format(username)

@app.route('/delcookie')
def delcookie():
    resp = make_response('<h1>Cookie is deleted Success</h1>')
    resp.delete_cookie('username')
    return resp

@app.route('/chgcookie')
def chgcookie():
    resp = make_response('</h1>Cookie is modified Success</h1>')
    resp.set_cookie('username', 'Acronymor')
    return resp

if __name__ == '__main__':
    app.run()
