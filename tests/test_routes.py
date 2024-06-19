import unittest
from app import create_app
import uuid


class TestRoutes(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client()
        self.app.config['TESTING'] = True

    def test_register_user(self):
        response = self.client.post('/auth/register', json={
            'username': f'test_user_{uuid.uuid4()}',
            'password': 'test_pass'
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn('user_id', response.get_json())

    def test_login_user(self):
        username = f'test_user_{uuid.uuid4()}'
        self.client.post('/auth/register', json={
            'username': username,
            'password': 'test_pass'
        })
        response = self.client.post('/auth/login', json={
            'username': username,
            'password': 'test_pass'
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.get_json())

    def test_protected_route_without_token(self):
        response = self.client.post('/account/create_account', json={
            'name': 'Alice',
            'initial_balance': 100.0,
            'currency': 'USD'
        })
        self.assertEqual(response.status_code, 401)

    def test_protected_route_with_token(self):
        username = f'test_user_{uuid.uuid4()}'
        self.client.post('/auth/register', json={
            'username': username,
            'password': 'test_pass'
        })
        login_response = self.client.post('/auth/login', json={
            'username': username,
            'password': 'test_pass'
        })

        token = login_response.get_json().get('access_token')

        response = self.client.post('/account/create_account', json={
            'name': 'Alice',
            'initial_balance': 100.0,
            'currency': 'USD'
        }, headers={'Authorization': f'Bearer {token}'})
        self.assertEqual(response.status_code, 201)


if __name__ == '__main__':
    unittest.main()
