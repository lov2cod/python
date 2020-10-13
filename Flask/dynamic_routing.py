
from flask import Flask

my_app = Flask(__name__)

@my_app.route("/")
def home():
    return "This is my home page"

@my_app.route("/silent/<int:number>")
def show_square(number):
    return "square of " + str(number) + " is: " + str(number*number)

if __name__ == "__main__":
    my_app.run(debug=True)