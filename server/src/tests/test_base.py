import os
import unittest2
from src import server


class TestBase(unittest2.TestCase):
    #def __init__(self):
        # TODO: change this to env var?
    base_dir = "/server/src/tests/"

    def setUp(self):
        server.config['TESTING'] = True
        server.config['WTF_CSRF_ENABLED'] = False
        server.config['DEBUG'] = False
        self.server = server.test_client()
        self.assertEqual(server.debug, False)

    def tearDown(self):
        pass

    def path(self, dir):
        return os.path.join(self.base_dir, dir)
