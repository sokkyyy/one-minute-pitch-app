from app import create_app,db
from flask_script import Manager,Server
from app.models import User,Pitch,Comment
from flask_migrate import Migrate, MigrateCommand


app = create_app('production')

migrate = Migrate(app,db)
manager = Manager(app)

manager.add_command('db',MigrateCommand)
manager.add_command('server',Server)

@manager.command
def test():
    '''
    Running unittests.
    '''
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Pitch=Pitch, Comment=Comment)



if __name__ == '__main__':
    manager.run()