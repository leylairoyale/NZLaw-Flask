from flask_sqlalchemy import SQLAlchemy
from chickenapp import app, login_manager
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin, login_user
from datetime import datetime
db = SQLAlchemy(app)

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(25), nullable = False)
    email = db.Column(db.String(150), unique = True, nullable = False)
    password = db.Column(db.String(256), nullable = False)
    contact = db.relationship('Contact', backref="client", lazy=True)
    review = db.relationship('Review', backref="client", lazy=True)

    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = self.set_password(password)

    def __repr__(self):
        return "{} was hatched.".format(self.username)

    #if something clucks up you can put in an init here but otherwise leave it
    #cause we shouldn't really need it.

    def set_password(self, password):
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash

    def check_password(self, password):
        return check_password_hash(self.password, password)

class Contact(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    contact = db.Column(db.String(500))
    date_create = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    

    def __repr__(self):
        return "{} wrote {} in contact.".format(self.name, self.contact)

    def __init__(self, name, contact, user_id):
        self.name = name
        self.contact = contact
        self.user_id = user_id

        #return "need this cause of repr I think."

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))
    review = db.Column(db.String(500))
    date_create = db.Column(db.DateTime)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    def __init__(self, name, review, user_id):
        self.name = name
        self.review = review
        self.user_id = user_id

    def __repr__(self):
        return "{} had {} to say about chicken lawyers.".format(self.name, self.review) 