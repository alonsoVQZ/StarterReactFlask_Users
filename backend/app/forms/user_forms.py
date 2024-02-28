from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length, Regexp

class SignupForm(FlaskForm):
    first_name = StringField('First Name', validators=[
        DataRequired(message='First name is required.'),
        Length(min=2, max=50, message='First name must be between 2 and 50 characters long.'),
        Regexp('^[A-Za-z][A-Za-z\'\-]+$', message="First name must contain only letters, apostrophes, or dashes.")
    ])
    last_name = StringField('Last Name', validators=[
        DataRequired(message='Last name is required.'),
        Length(min=2, max=50, message='Last name must be between 2 and 50 characters long.'),
        Regexp('^[A-Za-z][A-Za-z\'\-]+$', message="Last name must contain only letters, apostrophes, or dashes.")
    ])
    email = StringField('Email', validators=[
        DataRequired(message='Email is required.'),
        Email(message='Invalid email address.')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required.'),
        Length(min=8, message='Your password must be at least 8 characters long.'),
        Regexp(r'(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.*\W)', message='Your password must include at least one lowercase letter, one uppercase letter, one number, and one special character.')
    ])
    submit = SubmitField('SignUp')
    
class LoginForm(FlaskForm):
    email = StringField('Email', validators=[
        DataRequired(message='Email is required.'),
        Email(message='Invalid email address.')
    ])
    password = PasswordField('Password', validators=[
        DataRequired(message='Password is required.'),
    ])
    submit = SubmitField('Login')
    
