from flask import Flask, request, render_template
from .forms import RegisterFormContent
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html', name='Apktool')


@app.route('/register', methods=['POST', 'GET'])
def register():
    '''
    request.args, request.args, request.values
    1. 从URL 获取表单信息
    '''

    getParms = request.values

    '''
    get method
        request.form 不能获取到信息
        request.args 可以获取到信息
        request.values 可以获取到信息

    post method
        request.form 可以获取到信息
        request.args 可以获取到信息
        request.values 可以获取到信息
    '''

    mobile = getParms.get('mobile')
    password = getParms.get('password')
    password_repeat = getParms.get('password_repeat')
    mobile_code = getParms.get('mobile_code')

    print('---------break start-----------')
    print(mobile)
    print(password)
    print(password_repeat)
    print(mobile_code)
    print('---------break stop-----------')

    form = RegisterFormContent()

    form.mobile.data = mobile
    form.password.data = password
    form.password_repeat.data = password_repeat
    form.mobile_code.data = mobile_code

    '''
    form.mobile.data = '18566668888'
    form.password.data = '123456'
    form.password_repeat.data = '123456'
    form.mobile_code.data = '1579'
    '''
    return render_template('register.html', form=form)


# http://www.jianshu.com/p/ecd97b1c21c1
'''
url
http://127.0.0.1:5000/register?mobile=18566668888&password=123456&password_repeat=123456&mobile_code=1579
'''
