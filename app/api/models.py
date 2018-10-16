# Import the database object (db) from the main application module
# We will define this inside /app/__init__.py in the next sections.
from app import db

# Define a base model for other database tables to inherit
class Base(db.Model):

    __abstract__  = True

    id            = db.Column(db.Integer, primary_key=True)
    date_created  = db.Column(db.DateTime,  default=db.func.current_timestamp())
    

# Define a User model
class User(Base):

    __tablename__ = 'auth_user'

    # disease
    disease    = db.Column(db.String(500),  nullable=False)

    #medicine
    medicine    = db.Column(db.String(500),  nullable=False)

    # New instance instantiation procedure
    def __init__(self, disease, medicine):

        self.disease     = disease
        self.medicine    = medicine
        
    def __repr__(self):
        return '<User %r>' % (self.disease)                        

