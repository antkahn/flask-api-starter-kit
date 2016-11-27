import unittest
import json

from server import server
from models.abc import db
from models import User
from repositories import UserRepository


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def setUp(self):
        db.create_all()

    def tearDown(self):
        db.session.remove()
        db.drop_all()

    def test_get(self):
        """ The GET on `/user` should return an user """
        UserRepository.create(first_name='John', last_name='Doe', age=25)
        response = self.client.get('/application/user/Doe/John')

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json, {'user': {'age': 25, 'first_name': 'John', 'last_name': 'Doe'}})

    def test_create(self):
        """ The POST on `/user` should create an user """
        response = self.client.post(
            '/application/user/Doe/John',
            content_type='application/json',
            data=json.dumps({
                'age': 30
            })
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json, {'user': {'age': 30, 'first_name': 'John', 'last_name': 'Doe'}})
        self.assertEqual(User.query.count(), 1)

    def test_update(self):
        """ The PUT on `/user` should update an user's age """
        UserRepository.create(first_name='John', last_name='Doe', age=25)
        response = self.client.put(
            '/application/user/Doe/John',
            content_type='application/json',
            data=json.dumps({
                'age': 30
            })
        )

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(response_json, {'user': {'age': 30, 'first_name': 'John', 'last_name': 'Doe'}})
        user = UserRepository.get(first_name='John', last_name='Doe')
        self.assertEqual(user.age, 30)
