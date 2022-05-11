import unittest
from app import db 
from app.models import User


class UserTest(unittest.TestCase):
   def test_no_access_password(self):
            with self.assertRaises(AttributeError):
                self.new_user.password

def test_password_verification(self):
            self.assertTrue(self.new_user.verify_password('maureen'))


if __name__ == '__main__':
    unittest.main()