from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://python:Python@2017@localhost/testDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __repr__(self):
        return '<User %r>' % self.username

'''
temp.py

li@li-pc$ python3
>>> from temp import db, User
>>> db.create_all()  # 创建初始数据库
>>> admin = User('admin', 'admin@example.com')  # 创建数据
>>> guest = User('guest', 'guest@example.com')
>>> db.session.add(admin)   # 写入数据库
>>> db.session.add(guest)
>>> db.session.commit()
>>> users = User.query.all()  # 访问数据库中的数据
'''

