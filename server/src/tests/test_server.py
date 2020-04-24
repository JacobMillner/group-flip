from .test_base import TestBase


class ServerTests(TestBase):

    def test_main_page(self):
        response = self.server.get('/', follow_redirects=True)
        # we don't have a root route since we are an API, 404 for now
        self.assertEqual(response.status_code, 404)


if __name__ == "__main__":
    unittest2.main()
