from flask import Flask,render_template,redirect,url_for,request,make_response
app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/setcookie", methods = ['POST'])
def setcookie():
    if request.method == 'POST':
        user = request.form['nm']    
        resp = make_response(render_template('readcookie.html'))
        resp.set_cookie('userID', user)   
    return resp
@app.route("/getcookie")
def getcookie():
    name = request.cookies.get('userID')
    return '<h1>welcome '+name+'</h1>'

if __name__ == "__main__":
    #app.debug = True
    app.run(debug = True)
