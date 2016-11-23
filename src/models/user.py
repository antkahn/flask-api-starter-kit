"""
Define the User model
"""
from . import db
from .abc import BaseModel


class User(db.Model, BaseModel):
    """ The User model """
    __tablename__ = 'user'

    first_name = db.Column(db.String(300), primary_key=True)
    last_name = db.Column(db.String(300), primary_key=True)
    age = db.Column(db.Integer, nullable=True)

    def __init__(self, first_name, last_name, age=None):
        """ Create a new User """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
