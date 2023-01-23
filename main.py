from flask import request, make_response, redirect, render_template, session, url_for, flash
from app import create_app
from app.forms import LoginForm
import unittest


app = create_app()


app.config['SECRET_KEY'] = 'SUPER SECRETO'


todos = ["Finish this project", "Buy a coffe", "Sleep"]


@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    u = unittest.TextTestRunner()
    u.run(tests)


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
    username = session.get('username')
    context = {
        "user_ip": user_ip,
        "todos": todos,
        #"login_form": login_form,
        'username': username
    }
    return render_template("hello.html", **context)


if __name__ == "__main__":
   app.run(port=8080, debug=True)