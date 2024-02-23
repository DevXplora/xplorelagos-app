from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/Home')
def home():
    return render_template('Home.html')

@app.route('/AboutUs')
def about():
    return render_template('AboutUs.html')

@app.route('/Experience')
def experience():
    return render_template('Experience.html')
if  __name__ == '__main__':
    app.run(debug=True)
    
@app.route('/SignUp')
def signup():
    return render_template('SignUp.html')
if  __name__ == '__main__':
    app.run(debug=True)  
    
@app.route('/Sign')
def sign():
    return render_template('Sign.html')
if  __name__ == '__main__':
    app.run(debug=True)  
    
@app.route('/Select-adventure')
def selecta():
    return render_template('Select-adventure.html')

@app.route('/Select-culinary')
def selectc():
    return render_template('Select-culinary.html')

@app.route('/Select-cultural')
def selectcc():
    return render_template('/Select-cultural.html')

@app.route('/Select-luxury')
def luxury():
    return render_template('/Select-luxury.html')

@app.route('/TimeAndDate')
def TandD():
    return render_template('/TimeAndDate.html')


from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

