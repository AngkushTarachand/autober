import flask
from app import flask_app


@flask_app.route("/")
def index():
    return "Hackathon2"


@flask_app.route("/homepage")
def index_homepage():
    return flask.render_template("base.html")


@flask_app.route("/profile")
def profile_page():
    return flask.render_template("dashboard.html")
