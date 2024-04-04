from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Takeover By ya3raj"
