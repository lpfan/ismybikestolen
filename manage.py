from flask.ext.script import Manager

from proj import app


manager = Manager(app)

@manager.command
def runserver():
    app.run()

if __name__ == '__main__':
    manager.run()


