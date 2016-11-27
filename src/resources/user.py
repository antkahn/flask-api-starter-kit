"""
Define the REST verbs relative to the users
"""

from flask.ext.restful import Resource
from flask.ext.restful.reqparse import Argument
from flask.json import jsonify

from repositories import UserRepository
from util import parse_params


class UserResource(Resource):
    """ Verbs relative to the users """

    @staticmethod
    def get(last_name, first_name):
        """
        Return an user key information based on his name
        ---
        tags:
          - user
        parameters:
          - name: last_name
            in: path
            type: string
            description: the last name of the user
          - name: first_name
            in: path
            type: string
            description: the last name of the user
        responses:
          200:
            description: The user's information were successfully retrieved
            schema:
              example:
                user:
                  last_name: Doe
                  first_name: John
                  age: 30
        """
        user = UserRepository.get(last_name=last_name, first_name=first_name)
        return jsonify({'user': user.json})

    @staticmethod
    @parse_params(
        Argument(
            'age',
            location='json',
            required=True,
            help='The age of the user.'
        ),
    )
    def post(last_name, first_name, age):
        """
        Create an user based on the sent information
        ---
        tags:
          - user
        parameters:
          - name: last_name
            in: path
            type: string
            description: the last name of the user
          - name: first_name
            in: path
            type: string
            description: the last name of the user
          - name: body
            in: body
            schema:
              type: object
              properties:
                age:
                  type: integer
                  description: The age of the user
        responses:
          200:
            description: The user was successfully created
            schema:
              example:
                user:
                  last_name: Doe
                  first_name: John
                  age: 30
        """
        user = UserRepository.create(
            last_name=last_name,
            first_name=first_name,
            age=age
        )
        return jsonify({'user': user.json})

    @staticmethod
    @parse_params(
        Argument(
            'age',
            location='json',
            required=True,
            help='The age of the user.'
        ),
    )
    def put(last_name, first_name, age):
        """
        Create an user based on the sent information
        ---
        tags:
          - user
        parameters:
          - name: last_name
            in: path
            type: string
            description: the last name of the user
          - name: first_name
            in: path
            type: string
            description: the last name of the user
          - name: body
            in: body
            schema:
              type: object
              properties:
                age:
                  type: integer
                  description: The age of the user
        responses:
          200:
            description: The user was successfully created
            schema:
              example:
                user:
                  last_name: Doe
                  first_name: John
                  age: 30
        """
        repository = UserRepository()
        user = repository.update(
            last_name=last_name,
            first_name=first_name,
            age=age
        )
        return jsonify({'user': user.json})
