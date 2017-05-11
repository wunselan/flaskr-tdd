from app import app
import os
import unittest


class BasicTestCase(unittest.TestCase):

    def test_index(self):
        '''Initial test. Ensure Flask was set up correctly.'''
        tester = app.test_client(self)
        response = tester.get('/', content_type='html/text')

        self.assertEqual(response.status_code, 200)

    def test_database(self):
        '''Initial test. Ensure that the database exists.'''
        self.assertTrue(os.path.exists('flaskr.db'))


if __name__ == '__main__':
    unittest.main()
