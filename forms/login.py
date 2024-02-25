from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators

class LoginForm(FlaskForm): # Визначення класу форми для входу
    nickname = StringField("Nickname", [validators.DataRequired()], )
    password = PasswordField("Password", [validators.DataRequired()], )
    submit = SubmitField("Log in") # Кнопка для відправки форми