#!/usr/bin/python3.6
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "amiDMast Hello World edit from git!";
 
if __name__ == "__main__":
    app.run(debug = True, host = "0.0.0.0", port = 3000)
