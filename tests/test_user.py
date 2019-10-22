import unittest
from app.models import User,Pitch,Comment

class TestUser(unittest.TestCase):
    
    def setUp(self):
        self.new_user = User(username="ray",email="ndegwaray@gmail.com", password='12345',bio="www",pic_path="img/avatar.png")

    
    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure != None)
    
    def test_no_access_password(self):
        with self.assertRaises(AttributeError):
            self.new_user.password
    
    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('12345'))
    
    def test_instance_variables(self):
        self.assertEquals(self.new_user.username,"ray")
        self.assertEquals(self.new_user.bio,"www")
    
