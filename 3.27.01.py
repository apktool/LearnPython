# flask_script | Manager, Command

from flask_script import Manager, Command
from flask import Flask

app = Flask(__name__)
manager = Manager(app)


class haha(Command):
    def run(self):
        print("hello world")


manager.add_command('haha', haha())

# -------------------


@manager.command
def ahah():
    print("hello world")


if __name__ == '__main__':
    manager.run()
