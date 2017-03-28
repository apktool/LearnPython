# flask_script | Manager, Shell

from flask import Flask
from flask_script import Manager

app = Flask(__name__)
manager = Manager(app)


class haha():
    def fun():
        print('hello world')

# --------------------


@manager.shell
def make_shell_context():
    return dict(
        app=app,
        haha=haha,
    )

# --------------------


'''
# 本段代码是上述代码的本质，是基础的实现方式
from flask_script import Shell
def make_shell_context():
    return dict(
        app=app,
        haha=haha
    )

manager = Manager(app)
manager.add_command("shell", Shell(make_context=make_shell_context))
'''


if __name__ == '__main__':
    manager.run()


'''
python3 3.28.01.py shell
>>> haha.fun()
'''
