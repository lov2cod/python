
from flask import Flask, render_template

paws = Flask(__name__)

@paws.route("/")
def home():
    return render_template("paws_home.html")

@paws.route("/about")
def about():
    return render_template("paws_about.html")

if __name__ == "__main__":
    paws.run(debug=True)