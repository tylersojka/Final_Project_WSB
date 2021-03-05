import os
import pandas as pd

# os.environ

from flask import Flask, render_template, redirect
from flask_sqlalchemy import SQLAlchemy


#set up flask
app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv("postgres_uri")
pg = SQLAlchemy(app)


@app.route("/")
def index():
   return render_template("index.html")


if __name__ == "__main__":
   app.run(debug=True)