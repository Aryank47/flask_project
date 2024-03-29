from flask import Flask
app=Flask(__name__)

@app.route("/hello/<name>")
def hello_name(name):
    return "<br/><h1>Hello %s!</h1>"%name

if __name__=="__main__":
    app.run(debug=True)
