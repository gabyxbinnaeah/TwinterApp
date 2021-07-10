from django.test import TestCase
from models import Profile,Image
# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        '''
        method that creates instance of image 
        '''
        self.vin= Profile(profile_image="start.pgn",bio="Motivated IT geek")
        self.vin.save_profile()

        self.elly=Image(image="omollo.png",image_name="omollo",image_captions="beast",profile=self.vin,likes=700,comments="Taken at peak")
        self.elly.save_image()

    def test_image_instance(self):
        '''
        Method that checks if image is instanciated 
        '''
        self.assertTrue(isinstance(self.elly,Image))

