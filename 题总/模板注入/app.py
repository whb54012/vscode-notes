from flask import Flask, Request, render_template,render_template_string,session

app = Flask(__name__)
app.secret_key="whb54012"

@app.route("/self.html")
def index():
    username=Request.args.get("username")
    if():
        return render_template_string()
    else:
        return "登陆成功"+username
    