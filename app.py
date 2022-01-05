from flask import Flask, redirect, url_for, render_template, request
from flask.wrappers import Request

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html", content=True, x=4)

@app.route("/login", methods=["POST", "GET"])
def login():
    if request.method == "POST":
        user = request.form["name"]
        return redirect(url_for("user", usr=user))
    else:
        return render_template("login.html")

@app.route("/<usr>")
def user(usr):
    return f"<h1>Welcome {usr}!</h1>"

if __name__ == "__main__":
    app.run(debug=True)


