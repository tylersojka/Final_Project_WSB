import os
# os.environ

from flask import Flask, render_template, redirect


from flask_sqlalchemy import SQLAlchemy


# Obtain the configuration parameters
# params = config()

#set up flask
app = Flask(__name__)



# pg = SQLAlchemy(app)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ["postgres_uri"]
pg = SQLAlchemy(app)


@app.route("/")
def index():
   return render_template("index.html")


if __name__ == "__main__":
   app.run(debug=True)