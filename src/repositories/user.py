""" Defines the User repository """

from models import User


class UserRepository:
    """ The repository for the user model """

    @staticmethod
    def get(last_name, first_name):
        """ Query a user by last and first name """
        return User.query.filter_by(last_name=last_name, first_name=first_name).one()
