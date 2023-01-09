from flask import Flask, request, make_response, redirect


app = Flask(__name__)


@app.get("/")
def index():
    user_ip = request.remote_addr
    response = make_response(redirect("/hello"))
    response.set_cookie("user_ip", user_ip)
    return response


@app.get("/hello")
def hello():
    user_ip = request.cookies.get("user_ip")
    return (f"Hello world your IP:{user_ip}")


if __name__ == "__main__":
    app.run(port=8080, debug=True)