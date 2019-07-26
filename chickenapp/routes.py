from flask import render_template, redirect, url_for
from chickenapp import app
from chickenapp.models import db
from chickenapp.models import User, Contact, Review
from chickenapp.forms import Register, Login, ContactUs, ReviewUs
from flask_login import current_user, login_user, login_required, logout_user


@app.route("/")
def go_home():
    return render_template("index.html")

@app.route("/who_we_are")
def who_are():
    return render_template("whoweare.html")

@app.route("/what_we_do")
def what_do():
    return render_template("whatwedo.html")

@app.route("/signinsignup")
def sisu():
    form = Register()
    loginform = Login()
    return render_template('signinsignup.html', form=form, loginform=loginform)    

@app.route("/register", methods=["GET", "POST"])
def createChicken():
    form = Register()
    loginform = Login()
    if form.validate_on_submit():
        print("Ooh, cluck cluck {}".format(form.username.data))
        user = User(form.username.data, form.email.data, form.password.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for("go_home"))
    else:
        print("Nope, you cluckin' don't")
    return render_template("signinsignup.html", form=form, loginform=loginform)

@app.route("/login", methods=["GET", "POST"])
def login():
    form = Register()
    loginform = Login()
    #founduser = User.query.filter_by(username=loginform.username).first()
    if loginform.validate_on_submit():
        user = User.query.filter_by(username=loginform.username.data).first()
        if user is None or not user.check_password(loginform.password.data):
            print("no way buddy")
            return redirect(url_for('go_home'))
        login_user(user, remember=form.remember_me.data)
        print("chikasaw you in")
        return redirect(url_for("go_home"))
    else:
        print("nopity nope")
        return render_template("signinsignup.html", title="booo", form=form, loginform=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for("go_home"))

@app.route("/contact", methods=["GET", "POST"])
@login_required
def contactForm():
    form = ContactUs() 
    name = form.name.data 
    contact = form.contact.data
    user_id = current_user.id
    contacting = Contact(name, contact, user_id)  
    print(user_id, name, contact, form.errors)
    db.session.add(contacting)
    db.session.commit()
    return render_template("contact.html", form=form)

@app.route("/review", methods=["GET", "POST"])
@login_required
def reviewForm():
    form = ReviewUs()
    name = form.name.data
    review = form.review.data
    user_id = current_user.id 
    reviewing = Review(name, review, user_id)
    print(user_id, name, review, form.errors)
    db.session.add(reviewing)
    db.session.commit()
    return render_template("review.html", form=form)
