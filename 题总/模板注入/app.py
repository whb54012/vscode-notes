from flask import Flask, Request, render_template,render_template_string

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")