from flask import Flask, render_template, request, redirect, url_for

application = Flask(__name__)


@application.route('/')
def home():
    return "Login Successfully"


# Route for handling the login page logic
@application.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Login failed due to incorrect username and password'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

#run the server
if __name__ == '__main__':
    application.debug = True
    application.run()
