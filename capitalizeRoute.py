from datetime import datetime
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return "Hello, Rayef!"
    
@app.route("/<string:name>")
def hello(name):
    name = name.capitalize()
    return f"Hello, {name}!"
    

if __name__ == "__main__":
    app.run()
