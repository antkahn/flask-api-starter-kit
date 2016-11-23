"""
Defines the blueprint for the users
"""
from flask import Blueprint
from flask.ext.restful import Api

from resources import UserResource


USER_BLUEPRINT = Blueprint('user', __name__)
Api(USER_BLUEPRINT).add_resource(
    UserResource,
    '/user/<string:last_name>/<string:first_name>'
)
