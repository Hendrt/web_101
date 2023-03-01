from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def home_page():
    return "manchester united"




@app.route("/")
def about():
    return "this is the about page"



@app.route("/")
def home_page():
    return "render_template ("index.html")
