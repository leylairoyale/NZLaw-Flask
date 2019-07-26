from wtforms import Form, StringField, SubmitField, PasswordField, BooleanField, validators
from wtforms.validators import input_required, Email, EqualTo
from flask_wtf import FlaskForm

class Register(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    email = StringField("Email", validators=[input_required(), Email()])
    password = PasswordField("Password", validators=[input_required()])
    remember_me = BooleanField("Member me boo")
    confirm_pass = PasswordField("Confirm that cute lil password", validators=[input_required(), EqualTo('password')])
    submit = SubmitField()

class Login(FlaskForm):
    username = StringField("Username", validators=[input_required()])
    password = PasswordField("Password", validators=[input_required()])
    remember_me = BooleanField("Remember Meeeeeeee!")
    submit = SubmitField()

class ContactUs(FlaskForm):
    name = StringField("Name", validators=[input_required])
    contact = StringField("Contact", validators=[input_required()])
    submit = SubmitField()

class ReviewUs(FlaskForm):
    name = StringField("Name", validators=[input_required()])
    review = StringField("Review", validators=[input_required()])
    submit = SubmitField()