import flask_wtf
import wtforms


class Login(flask_wtf.Flaskform):
    first_name = wtforms.StringField("First Name")
    last_name = wtforms.StringField("Last Name")
    email = wtforms.StringField("Email")
    password = wtforms.PasswordField("Password")
    confirm_password = wtforms.PasswordField("Confirm Password")

    submit = wtforms.SubmitField("Submit")


class Register(flask_wtf.FlaskForm):
    first_name = wtforms.StringField("First Name")
    last_name = wtforms.StringField("Last Name")
    email = wtforms.StringField("Email")
    password = wtforms.PasswordField("Password")

    submit = wtforms.SubmitField("Submit")



