from flask import Flask, Request, render_template,render_template_string,session,redirect, url_for

app = Flask(__name__)
app.secret_key="whb54012"

@app.route("/")
def index():
    uname=Request.form.get("username","")
    pwd=Request.form.get("password","")
    if uname and pwd:
        session['username']=uname
        return redirect(url_for("self.html"))
    else:
        return render_template("index.html")
@app.route("/self.html")
def index():   
    if not session.get('username'):
        return redirect(url_for("/"))
    elif session['username']=='admin':
        uname=session['username']
        u=Request.args.get("username","")
        return render_template_string("你好"+u)
    else:
        uname=session['username']
        return "登陆成功"+uname
    