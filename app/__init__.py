import os
from dotenv import load_dotenv
from flask import Flask
from models.base import Session, create_db
from flask_login import LoginManager

load_dotenv()

app = Flask(__name__)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
# Ініціалізація Flask-Login
login_manager = LoginManager()
login_manager.login_view = "login"
login_manager.init_app(app)


create_db()

from models import User, Event


@login_manager.user_loader # загрузи дані про нас
def load_user(user_id: int):
    with Session() as session:
        return session.query(User).where(User.id == user_id).first()

import routes