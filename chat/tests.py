from django.test import TestCase
from .models import Profile,Image
# Create your tests here.

class ImageTestClass(TestCase):
    def setUp(self):
        '''
        method that creates instance of image 
        '''
        self.vin= Profile(profile_photo="start.pgn",bio="Motivated IT geek")
        self.vin.save_profile()

        self.elly=Image(image="omollo.png",image_name="omollo",image_captions="beast",profile=self.vin,likes=700,comments="Taken at peak")
        self.elly.save_image()

    def test_image_instance(self):
        '''
        function that checks if image is instanciated 
        '''
        self.assertTrue(isinstance(self.elly,Image))

    def test_save_image(self):
        '''
        Method that test if image model is saved 
        '''
        self.elly.save_image()
        image_list=Image.objects.all()
        self.assertTrue(len(image_list)>0) 

    def test_image_delete(self):
        '''
        method that checks if image is saved 
        '''
        self.elly.save_image()
        self.elly.delete_image()
        check_list=Image.objects.all()
        self.assertTrue(len(check_list)==0)

        


