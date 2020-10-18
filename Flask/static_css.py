from flask import Flask, render_template

app_static = Flask(__name__)

@app_static.route("/")
def home():
    return render_template("home_static_css.html")

if __name__ == "__main__":
    app_static.run(debug=True)