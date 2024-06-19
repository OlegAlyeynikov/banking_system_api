import unittest
from app.services.account_services import create_account_service
from app.models import accounts


class TestServices(unittest.TestCase):
    def setUp(self):
        accounts.clear()

    def test_create_account_service(self):
        data = {'name': 'Alice', 'initial_balance': 100.0}
        response, status_code = create_account_service(data)
        self.assertEqual(status_code, 201)
        self.assertIn('account_id', response)


if __name__ == '__main__':
    unittest.main()
