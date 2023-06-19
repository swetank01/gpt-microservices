from .database import db

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(50), nullable=False)

    # Add any other attributes and relationships as needed

    def __init__(self, name, email):
        self.name = name
        self.email = email
