from flask import Flask, render_template, request, flash
from flask.helpers import get_flashed_messages
from db_routines import DbRoutines

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'                          #SQL Setup
app.config['MYSQL_USER'] = 'root'                                           #SQL Setup
app.config['MYSQL_PASSWORD'] = 'root_password'                              #SQL Setup
app.config['MYSQL_HOST'] = 'db'                                             #SQL Setup
app.config['MYSQ_PORT'] = 3306                                              #SQL Setup
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'                              #SQL Setup

dbRoutines = DbRoutines(app)

is_registered_user = False

#Base Page
@app.route('/')
def index():
    return render_template("index.html")

#Login page
@app.route('/login', methods=['POST', 'GET'])
def login():
    return render_template("login.html")

#signup page
@app.route('/sign_up', methods=['POST', 'GET'])
def sign_up():
    if request.method == 'POST':
        if request.form['uname'] != "" and request.form['pwd'] != "" and request.form['repwd'] != "" and request.form['pwd'] == request.form['repwd']: #Check passwords match and fields aren't blank
            userName = request.form['uname']                                                                                                           #Request username
            userPwd = request.form['pwd']                                                                                                              #Request password
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute(f"SELECT COUNT(*) FROM `Credentials` WHERE username = '{userName}' AND userpwd = '{userPwd}';")                             #Check credentials against DB

            user_list = cursor.fetchall()
            if user_list[0]['COUNT(*)'] > 0:                                                                                                            #Check credentials against DB
                cursor.close()
                flash('Account already registered', category='error')                                                                                   #Throw error message
                return render_template("sign_up.html")                                                                                                  #Return to signup
            else:
                cursor.execute(f"INSERT INTO `Credentials` (`username`, `userpwd`) VALUES ('{userName}','{userPwd}');")                                 #Add user to DB credentials
                dbRoutines.mysql.connection.commit()
                cursor.close()
                flash('User created', category='success')                                                                                               #Throw success message
                return render_template("login.html")                                                                                                    #Route to login page
        else:
            flash('Invalid input', category='error')                                                #Throw error message
            return render_template("sign_up.html")                                                  #Return to signup page

    return render_template("sign_up.html")                                                          #Return to signup page

#main page
@app.route('/main', methods=['POST', 'GET'])
def main():
        if request.method == 'POST':
            race = request.form['race']                                                                                                                 #Request race
            weapon = request.form['weapon']                                                                                                             #Request weapon
            armor = request.form['armor']                                                                                                               #Request armor
            primary_stat = request.form['primary_stat']                                                                                                 #Request primary stat
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute(f"INSERT INTO `Template` (`race`, `weapon`, `armor`, `primary_stat`) VALUES ('{race}', '{weapon}', '{armor}', '{primary_stat}');")   #Add user choices to DB
            dbRoutines.mysql.connection.commit()                                            
            cursor.close()
            flash('Character created', category='success')                                          #Throw success message
            return render_template("main.html")                                                     #Return to main page

#verify page
@app.route('/verify', methods=['POST'])
def verify():
    if request.method == 'POST':
        if request.form['uname'] != "" and request.form['pwd'] != "":                                                                                   #Check forms aren't blank
            userName = request.form['uname']                                                                                                            #Request username
            userPwd = request.form['pwd']                                                                                                               #Request password
            cursor = dbRoutines.mysql.connection.cursor()
            cursor.execute(f"use webapp_db;")
            cursor.execute(f"SELECT COUNT(*) FROM `Credentials` WHERE username = '{userName}' AND userpwd = '{userPwd}';")                              #Check user against DB

            user_list = cursor.fetchall()
            if user_list[0]['COUNT(*)'] > 0:
                cursor.close()
                flash('Logged In', category='success')                                              #Throw success message
                return render_template('main.html')                                                 #Reroute to main page
        else:
            flash('Invalid credentials', category='error')                                          #Throw error message
    return render_template("login.html")                                                            #Return to login page
            

            



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