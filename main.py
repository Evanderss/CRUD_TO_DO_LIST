from flask import Flask


app = Flask(__name__)


@app.get("/")
def hello():
    return "Hello world"


if __name__ == "__main__":
    app.run(port=8080)