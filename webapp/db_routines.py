from flask_mysqldb import MySQL

class DbRoutines():
    def __init__(self, app):
        self.mysql = MySQL()
        self.mysql.init_app(app)

    def say_hello(self):
        return "Hello there..."


