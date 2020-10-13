
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello here i come"

@app.route("/air")
def intro():
    return "Hello guysss"

if __name__ == "__main__":
    app.run()


