
from flask import Flask

paws = Flask(__name__)

@paws.route("/")
def home():
    return "Paws Rescue Center"

@paws.route("/about")
def about():
    return "\"We are a non-profit organization working as an animal rescue.\
    We aim to help you connect with the purrfect furbaby for you! \
    The animals you find on our website are rescued and rehabilitated animals. \
    Our mission is to promote the ideology \"adopt, don't hop \"! \""

if __name__ == "__main__":
    paws.run(debug=True)