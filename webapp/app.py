import re
from flask import Flask, render_template, request, flash
from flask.helpers import get_flashed_messages
from db_routines import DbRoutines

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root_password'
app.config['MYSQL_HOST'] = 'db'
app.config['MYSQ_PORT'] = 3306
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

dbRoutines = DbRoutines(app)

is_registered_user = False

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template("login.html")

@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        if request.form['uname'] != "" and request.form['pwd'] != "" and request.form['repwd'] != "" and request.form['pwd'] == request.form['repwd']:
            userName = request.form['uname']
            userPwd = request.form['pwd']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute(f"SELECT COUNT(*) FROM `Credentials` WHERE username = '{userName}' AND userpwd = '{userPwd}';")

            user_list = cursor.fetchall()
            if user_list[0]['COUNT(*)'] > 0:
                cursor.close()
                flash('Account already registered', category='error')
                return render_template("sign_up.html")
            else:
                cursor.execute(f"INSERT INTO `Credentials` (`username`, `userpwd`) VALUES ('{userName}','{userPwd}');")
                dbRoutines.mysql.connection.commit()
                cursor.close()
                flash('User created', category='success')
                return render_template("login.html")
        else:
            flash('Invalid input', category='error')
            return render_template("sign_up.html")

    return render_template("sign_up.html")


@app.route('/main', methods=['POST', 'GET'])
def main():
    return render_template("main.html")

@app.route('/verify', methods=['POST'])
def verify():
    if request.method == 'POST':
        if request.form['uname'] != "" and request.form['pwd'] != "": 
            userName = request.form['uname']
            userPwd = request.form['pwd']
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute(f"SELECT COUNT(*) FROM `Credentials` WHERE username = '{userName}' AND userpwd = '{userPwd}';")

            user_list = cursor.fetchall()
            if user_list[0]['COUNT(*)'] > 0:
                cursor.close()
                flash('Logged In', category='success')
                return render_template('main.html')
               
            

            
        else:
            flash('Invalid credentials', category='error')
    return render_template("login.html")


@app.route('/help/<subject>')
def help(subject):
    return render_template('help.html', message=subject)

@app.route('/help')
def xhelp():
    return render_template('help.html')

if __name__ == '__main__':
   app.run(host='0.0.0.0', debug=True)

   # TODO: Make server production grade using 'waitress'






"""


"""

"""
@app.route('/help', methods=['GET'])
def help():

    msg = ""

    if request.method == 'GET':
        help_type = request.args.get('subject')

    if help_type == 'login':
        msg = 'You need to provide both name and password.'

    if help_type == 'forgot':
        msg = 'You need to contact your support desk.'

    return render_template('help.html', message=msg)

"""