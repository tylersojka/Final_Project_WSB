import sys
sys.path.append(".")
from flask import Flask, render_template, redirect
# Import the 'config' function from the config.py file
from Postgres.config import config

from flask_sqlalchemy import SQLAlchemy



# Obtain the configuration parameters
params = config()




#set up flask
app = Flask(__name__)

#use flask_sqlalchemy to set up postgres connection
app.config["SQLALCHEMY_DATABASE_URI"] = f"postgresql://{params['user']}:{params['password']}@{params['host']}/{params['production_database']}"  #connect to postgres 
pg = SQLAlchemy(app)



@app.route("/")
def index():
   return render_template("index.html")









if __name__ == "__main__":
   app.run(debug=True)