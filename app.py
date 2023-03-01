from flask import Flask


app = Flask(__name__)

@app.route("/")
def home_page():
    return "manchester united"




@app.route("/")
def about():
    return "this is the about page"

