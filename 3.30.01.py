# flask | Jinja2基本

from flask import Flask
from flask import render_template

app = Flask('heh')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)


if __name__ == '__main__':
    app.run()


'''
3.30.01.py
templates
├── index.html
└── user.html
'''

# index.html
'''
<h1>hello world</h1>
'''

# user.html
'''
<h1>hello, {{ name|capitalize }}!</h1>
'''

# Jinja2变量过滤器
'''
safe 渲染值时不转义
capitalize 把值的首字母转换成大写,其他字母转换成小写
lower 把值转换成小写形式
upper 把值转换成大写形式
title 把值中每个单词的首字母都转换成大写
trim 把值的首尾空格去掉
striptags 渲染之前把值中所有的 HTML 标签都删掉
'''
