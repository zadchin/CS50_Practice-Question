from flask import Flask, flash, redirect, render_template, request, session, url_for
from flask_session import Session

app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Secret key needed to use sessions
app.config['SECRET_KEY'] = '12345'

# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Dummy credentials for demonstration
correct_username = "zadchin@gmail.com"
correct_password = "CS50@123"

@app.route('/', methods=['GET', 'POST'])
def login():
    # Check if the user is already logged in
    if 'username' in session:
        return render_template('welcome.html')

    ## YOUR CODE HERE
    

@app.route('/welcome')
def welcome():
    # Check if user is logged in
    if 'username' in session:
        # Show the welcome page
        return render_template('welcome.html')
    else:
        # If not logged in, redirect to login page
        return redirect(url_for('login'))

@app.route('/logout')
def logout():
    # Remove the username from the session if it's there
    session.pop('username', None)
    # Redirect to login page
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
