from flask_wtf import FlaskForm
from wtforms import PasswordField,StringField,SubmitField
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import ValidationError


class RegistrationForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    username=StringField("Username",validators=[DataRequired()])
    password=PasswordField("Password",validators=[DataRequired(),EqualTo('pass_confirm',message='Password must match!')])
    pass_confirm=PasswordField("Confirm Password",validators=[DataRequired()])
    submit=SubmitField('Register!')

    def check_email(self,field):
        if User.query.fitler_by(email=field.data).first():
            raise ValidationError("your email has been already registered!")

    def check_email(self,field):
        if User.query.fitler_by(username=field.data).first():
            raise ValidationError("Username is taken")

class LoginForm(FlaskForm):
    email=StringField('Email',validators=[DataRequired(),Email()])
    password=PasswordField("Password",validators=[DataRequired()])
    submit=SubmitField('Log In')
