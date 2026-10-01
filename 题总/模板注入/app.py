from flask import Flask, Request, render_template,render_template_string,session,redirect, url_for

app = Flask(__name__)
app.secret_key="whb54012"

@app.route("/",methods=["GET","POST"])
def index():
    uname=Request.form.get("username","")
    pwd=Request.form.get("password","")
    if uname and pwd:
        session['username']=uname
        return redirect(url_for("self"))
    else:
        return render_template("index.html")
@app.route("/self.html")
def self():   
    if not session.get('username'):
        return redirect(url_for("index"))
    elif session['username']=='admin':
        uname=session['username']
        u=Request.args.get("param","")
        return render_template_string("你好"+uname+u)
    else:
        return "登陆成功"+uname
    