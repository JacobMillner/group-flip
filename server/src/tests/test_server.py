import os
import unittest2
from src import server


class ServerTests(unittest.TestCase):
    def setUp(self):
        server.config['TESTING'] = True
        server.config['WTF_CSRF_ENABLED'] = False
        server.config['DEBUG'] = False
        self.server = server.test_client()
        self.assertEqual(server.debug, False)

    def tearDown(self):
        pass

    def test_main_page(self):
        response = self.server.get('/', follow_redirects=True)
        self.assertEqual(response.status_code, 200)


if __name__ == "__main__":
    unittest2.main()
