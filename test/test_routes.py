import unittest
import json

from server import server


class TestUser(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.client = server.test_client()

    def test_get(self):
        """ The GET on `/routes` should return the list of the API's routes """
        self.maxDiff = None
        response = self.client.get('/application/routes')

        self.assertEqual(response.status_code, 200)
        response_json = json.loads(response.data.decode('utf-8'))
        self.assertEqual(len(response_json['routes']), 6)
