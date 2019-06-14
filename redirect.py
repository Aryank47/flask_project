from flask import Flask, redirect, url_for, render_template, request
# Initialize the Flask application
app = Flask(__name__)

@app.route('/')
def index():
   return render_template('login.html')

@app.route('/login',methods = ['POST', 'GET'])
def login():
   if request.method == 'POST' and request.form['username'] == 'admin' :
       return redirect(url_for('success'))
   return redirect(url_for('index'))

@app.route('/success')
def success():
   return '<h1>logged in successfully</h1>'
	
if __name__ == '__main__':
   app.run(debug = True)

