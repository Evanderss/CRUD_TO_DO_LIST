from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired


app = Flask(__name__)
bootstrap = Bootstrap(app)


app.config['SECRET_KEY'] = 'SUPER SECRETO'


todos = ["Finish this project", "Buy a coffe", "Sleep"]


class LoginForm(FlaskForm):
    username = StringField("Username: ", validators=[DataRequired()])
    password = PasswordField("Password: ", validators=[DataRequired()])
    submit = SubmitField("Send")


@app.errorhandler(404)
def not_found(error):
    return render_template('404.html', error=error)


@app.get("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    session["user_ip"] = user_ip
    return response


@app.get("/hello")
def hello():
    user_ip = session.get("user_ip")
    login_form = LoginForm()
    context = {
        "user_ip": user_ip,
        "todos": todos,
        "login_form": login_form
    }
    return render_template("hello.html", **context)


if __name__ == "__main__":
   app.run(port=8080, debug=True)