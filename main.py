from flask import Flask, request, make_response, redirect, render_template, session
from flask_bootstrap import Bootstrap


app = Flask(__name__)
bootstrap = Bootstrap(app)


app.config['SECRET_KEY'] = 'SUPER SECRETO'


todos = ["Finish this project", "Buy a coffe", "Sleep"]


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
    context = {
        "user_ip": user_ip,
        "todos": todos
    }
    return render_template("hello.html", **context)


if __name__ == "__main__":
   app.run(port=8080, debug=True)