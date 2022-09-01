import flask
from app import flask_app


@flask_app.route("/")
def index():
    return "Hackathon2"


@flask_app.route("/homepage")
def sign_in():
    return flask.render_template("dashboard.html")
