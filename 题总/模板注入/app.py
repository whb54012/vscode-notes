from flask import Flask, Request, render_template,render_template_string,session

app = Flask(__name__)
app.secret_key="whb54012"

@app.route("/self.html")
def index():
    uname=Request.args.get("username")
    session['username']=uname
    if(session['username']=='admin'):
        return render_template_string()
    else:
        return "登陆成功"+uname
    