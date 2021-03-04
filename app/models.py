from datetime import datetime
from app import db


class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    name = db.Column(db.String(120), unique = True, nullable=False)
    image_file = db.Column(db.String(120), unique=True, nullable=False)
    description = db.Column(db.String(300), nullable= False)

    def __repr__(self):
        return f"Pizza('{self.id}'', '{self.name}','{self.image_file},'{self.description}'"

