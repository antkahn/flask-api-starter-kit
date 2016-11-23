"""
Define the REST verbs relative to the users
"""

from flask.ext.restful import Resource
from flask.json import jsonify

from repositories import UserRepository


class UserResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    def get(last_name, first_name):
        """ Return a list of key information about users """
        user = UserRepository.get(last_name=last_name, first_name=first_name)
        return jsonify({'user': user.json})
