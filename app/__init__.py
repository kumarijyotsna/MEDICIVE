# Import flask and template operators
from flask import Flask, render_template

# Import SQLAlchemy
from flask_sqlalchemy import SQLAlchemy

# Define the WSGI application object
app = Flask(__name__)

# Configurations
app.config.from_object('config')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
# Define the database object which is imported
# by modules and controllers
db = SQLAlchemy(app)

#Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

# Import a module / component using its blueprint handler variable (medicive)
from app.api.api1 import medcive
from app.api.api2 import medcive
from app.api.api3 import medcive
from app.api.api4 import medcive
from app.api.api5 import medcive
from . import api

# Register blueprint(s)
app.register_blueprint(api.medcive)

# Build the database:
# This will create the database file using SQLAlchemy
db.create_all()

