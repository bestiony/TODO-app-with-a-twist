from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/", methods = ["POST","GET"])
def index():
    if request.method == "POST":
        return 
        
    return render_template("index.html")
