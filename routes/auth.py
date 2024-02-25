from app import app
from forms import LoginForm, RegistrationForm
from flask import render_template, redirect, flash
from models import User, Session
from flask_login import login_user
from werkzeug.security import generate_password_hash, check_password_hash


@app.route("/signup", methods=["GET", "POST"])
def registration():
    form = RegistrationForm()
    if form.validate_on_submit():
        with Session() as session:
            user = session.query(User).where(User.email == form.email.data).first()
            if user:
                flash("User currently exists")
                redirect("/login")
            user = User(
                nickname=form.email.data.split('@')[0],
                email=form.email.data,
                password=generate_password_hash(form.password.data)
            )

            try:
                session.add(user)
                session.commit()
                return redirect("/login")
            except Exception as exc:
                return f"{exc}"
            finally:
                session.close()
    return render_template("form_template.html", form=form)


@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        with Session() as session:
            user = session.query(User).where(User.nickname == form.nickname.data).first()
            if user:
                if check_password_hash(user.password, form.password.data):
                    login_user(user)
                    return redirect("/")
            flash("Wrong password")
            return redirect("/login")
    return render_template("form_template.html", form=form)
