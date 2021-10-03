from dotenv import load_dotenv
from flask import Flask

load_dotenv()

app = Flask(__name__)


@app.route("/")
def home():
    return "<h2>Well, hello there.</h2>"
