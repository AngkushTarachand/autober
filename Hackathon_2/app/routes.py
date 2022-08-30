import flask
from app import flask_app


@flask_app.route("/")
def index():
    return "Hackathon2"


@flask_app.route("/sign_in")
def sign_in():
    return "WIP"
