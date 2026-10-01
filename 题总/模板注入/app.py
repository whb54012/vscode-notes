from flask import Flask, Request, render_template,render_template_string,session

app = Flask(__name__)
app.secret_key="whb54012"

@app.route("/")
def index():
    uname=Request.args.get("username")
    session['username']=uname
@app.route("/self.html")
def index():   
    if(session.get(username)):
         return render_template()
    elif(session['username']=='admin'):
        return render_template_string()
    else:
        uname=session['username']
        return "登陆成功"+uname
    