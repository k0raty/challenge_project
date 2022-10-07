from flask import Flask, render_template      

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('home.html') #looks for python templates and install it.
    
@app.route("/salvador")
def salvador():
    return "Hello, Salvador"
    
if __name__ == "__main__":
    app.run(debug=True)
