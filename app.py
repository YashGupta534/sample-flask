from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from Flaskv1"

@app.route("/test")
def test():
    return "Test Endpoint"

@app.route("/new")
def new():
    return "Latest Image"

if __name__ == "__main__":
    app.run(debug=False)