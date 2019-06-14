from flask import Flask  
app = Flask(__name__)  

@app.route("/hello")      
def about():  
    return "This is about page";  
      
  
      
if __name__ =="__main__":  
    app.run(debug = True)
    app.add_url_rule("/about","about",about)
