from flask import Flask
from flask_script import Shell, Manager, Server
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()


class User(db.Model):
    __tablename__ = 'user_table_name'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(255))
    password = db.Column(db.String(255)) 

def make_shell_context():
    return dict(app=app,db=db)

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
manager = Manager(app)
manager.add_command('shell', Shell(make_context=make_shell_context))

@app.route('/')
def index():
    return "<User `{}`>".format(self.username)

if __name__ == '__main__':
    manager.run()
