import unittest
from app.models import User

class UserModelTest(unittest.TestCase):

  def setUp(self):
    """  
    This is specifically to test our password hashing feature.

    Please note that we are using a password property and not
    password_hash as we defined in our models.
    """
    self.test_user = User(password = 'thisisatest')


  def test_password_hashing(self):
    """  
    Function that check that a password_hash is generated.
    """
    self.assetTrue(self.test_user.password_hash is not None)

  def test_write_only_pass(self):
    """  
    Function to check if AttributeError is raised when someone tries
    to read.
    """
    with self.assertRaises(AttributeError):
      self.test_user.password

  def test_pass_verification(self):
    """  
    Function returns a boolean if the password_hash for thisisatest
    is the same as the one generated when hashing it the first time.
    """
    self.assetTrue(self.test_user.verify_password('thisisatest'))