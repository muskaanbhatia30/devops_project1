from flask import Flask
app = Flask(__name__)


@app.route("/info")
def lwinfo():
 return "i m LW from India"

@app.route("/phone")
def lwphone() :
 return "9351009002"


if __name__ == "__main__":
    app.run(host="0.0.0.0")