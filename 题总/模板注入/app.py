from flask import Flask, Request, render_template,render_template_string,session

app = Flask(__name__)
app.secret_key="whb54012"

@app.route("/")
def index():
    uname=Request.args.post("username","")
    pwd=Request.args.post("password","")
    if 
    session['username']=uname
@app.route("/self.html")
def index():   
    if not session.get('username'):
         return render_template()
    elif session['username']=='admin':
        uname=session['username']
        u=Request.args.get("username","")
        return render_template_string("你好"+u)
    else:
        uname=session['username']
        return "登陆成功"+uname
    