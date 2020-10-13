
from flask import Flask

aj = Flask(__name__)

@aj.route("/")
def home():
    return "This is my home page"

@aj.route("/<my_name>")
def greetings(my_name):
    return "welcome " + my_name + "!"

if __name__ == "__main__":
    aj.run(debug=True)