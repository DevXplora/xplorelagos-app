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
    
#@app.route('/signup')
#def signup():
#    return render_template('signup.html')
#if  __name__ == '__main__':
 #   app.run(debug=True)  
    
#@app.route('/signin')
#def sign():
#    return render_template('Signin.html')
#if  __name__ == '__main__':
#    app.run(debug=True)  
    
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

## Athentication 
from flask import Flask, render_template, redirect, url_for, flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Length
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt


app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    
class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign Up')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    
    
@app.route('/')
def index():
    return render_template('Home.html')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(username=form.username.data, email=form.email.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash('Your account has been created!', 'success')
        return redirect(url_for('signin'))
    return render_template('signup.html', form=form)

@app.route('/signin', methods=['GET', 'POST'])
def signin():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check email and password.', 'danger')
    return render_template('signin.html', form=form)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)

