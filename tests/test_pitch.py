import unittest
from app.models import User,Pitch,Comment

class TestPitch(unittest.TestCase):


    def setUp(self):
        self.new_user = User(username="ray",email="ndegwaray@gmail.com", password='12345',bio="www",pic_path="img/avatar.png")
        self.new_pitch = Pitch(pitch_category="general",pitch_details="rrrr",upvote=0,downvote=0,user=self.new_user)
        self.new_comment = Comment(pitch_comment="ghghgh",pitch=self.new_pitch,comment_user=self.new_user)
    
    def tearDown(self):
        User.query.delete()
        Pitch.query.delete()
        Comment.query.delete()

    def test_instance_variables(self):
        self.assertEquals(self.new_pitch.pitch_category,"general")
        self.assertEquals(self.new_pitch.pitch_details,"rrrr")
        self.assertEquals(self.new_pitch.upvote,0)
        self.assertEquals(self.new_pitch.downvote,0)
        self.assertEquals(self.new_pitch.user, self.new_user)
    
    def test_save_pitch(self):
        self.new_pitch.save_pitch()
        self.assertEquals(len(Pitch.query.all()),1)

    def test_like_pitch(self):
        self.new_pitch.like_pitch()

    
   
    
