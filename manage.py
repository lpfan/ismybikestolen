from flask.ext.script import Manager

from proj import app
from api import api


manager = Manager(app)

@manager.command
def runserver():
    api.app = app
    app.run()

if __name__ == '__main__':
    manager.run()


