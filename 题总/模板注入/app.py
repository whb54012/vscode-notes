from flask import Flask, request, render_template,render_template_string,session,redirect, url_for

app = Flask(__name__)
app.secret_key="whb54012"

@app.route("/",methods=["GET","POST"])
def index():
    uname=request.form.get("username","")
    pwd=request.form.get("password","")
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
        u=request.args.get("param","")
        list=['__class__','__init__']
        if any(u in w for w in list):
            return render_template_string("违规字符")
        return render_template_string("你好"+uname+u)
    else:
        return "登陆成功"
if __name__ == '__main__':
    app.run(debug=True)
    