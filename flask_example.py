from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "hello world"

app.run('0.0.0.0')