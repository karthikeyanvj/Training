from flask import Flask, render_template, request, session, url_for, redirect
from flask_mysqldb import MySQL

login = Flask(__name__)
login.secret_key = "#gydgvdsfkgdfw4587yt45g"

login.config['MYSQL_HOST'] = 'localhost'
login.config['MYSQL_USER'] = 'root'
login.config['MYSQL_PASSWORD'] = ''
login.config['MYSQL_DB'] = 'kar'

mysql = MySQL(login)
print("success")


@login.route("/")
def home():
    return render_template("home.html")


@login.route("/signup")
def signup_page():
    return render_template("Sign_up.html")


@login.route("/signup_data", methods=['POST', 'GET'])
def signup_data():
    if request.method == "POST":
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        age = request.form['age']
        college = request.form['college']
        degree = request.form['degree']
        city = request.form['city']
        cur = mysql.connection.cursor()
        sql = "INSERT INTO studentdetails (name,email,password,age,college,degree,city) VALUES (%s,%s,%s,%s,%s,%s,%s)"
        val = (name, email, password, age, college, degree, city)
        cur.execute(sql, val)
        mysql.connection.commit()
        cur.close()
        return render_template("display.html")


@login.route("/logging")
def logging():
    return render_template("login_page.html")


@login.route("/login_data", methods=['POST', 'GET'])
def login_data():
    error_message = ''
    if request.method == 'POST':
        uname = request.form.get('username')
        password = request.form.get('password')
        if len(uname) == 0 and len(password) == 0:
            error_message = "Username and password is empty "
        elif len(uname) == 0:
            error_message = "Username is empty"
        elif len(password) < 5:
            error_message = "Password is empty"
        else:
            sql = "SELECT * FROM studentdetails WHERE name = %s AND password = %s"
            val = uname, password
            cur = mysql.connection.cursor()
            cur.execute(sql, val)
            mysql.connection.commit()
            cur.close()
            countRows = cur.rowcount
            if countRows < 1:
                error_message = "Invalid Login credentials"
            else:
                return redirect(url_for('profile'))

    return render_template('login_page.html', error="OOPS !! " + error_message)


@login.route('/profile', methods=['post', 'get'])
def profile():



if __name__ == "__main__":
    login.run(debug=True)
