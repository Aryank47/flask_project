from flask import Flask
app=Flask(__name__)

@app.route("/")
def hello():
    return "</br><h2>Hello World! welcome!</h1>"

if __name__=="__main__":
    #app.debug=True
    app.run(debug=True)
