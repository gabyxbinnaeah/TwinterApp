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
        method that checks if image is delete_image method deletes image 
        '''
        self.elly.save_image()
        self.elly.delete_image()
        check_list=Image.objects.all()
        self.assertTrue(len(check_list)==0)


    def test_caption_update(self):
        '''
        method that checks if caption is updates
        '''
        self.elly.save_image()
        self.elly.update_caption(self.elly.id,'gabs')
        image_list=Image.objects.all()
        self.assertTrue(len(image_list)==1)
        updated_caption=Image.objects.all().first()
        self.assertTrue(updated_caption.image_captions=='gabs') 




class ProfileTestClass(TestCase):
    def setUp(self):
        '''
        Method that creates instance of profile class
        '''
        self.vin= Profile(profile_photo="start.pgn",bio="Motivated IT geek")
        self.vin.save_profile()

    def test_instance(self):
        '''
        method that checks if profile is instance
        '''
        self.assertTrue(isinstance(self.vin,Profile))


    def test_save_profile(self):
        '''
        Method that test if profile is being saved
        '''
        self.vin.save_profile()
        list_profile=Profile.objects.all()
        self.assertTrue(len(list_profile)>0) 

    def test_delete_profile(self):
        '''
        method that checks if profile is deleted
        '''
        self.vin.save_profile()
        self.vin.delete_profile()
        left_profiles=Profile.objects.all()
        self.assertTrue(len(left_profiles)==0) 

    def test_bio_update(self):
        '''
        method that checks if bio can be updated
        '''
        self.vin.save_profile()
        self.vin.update_profile_bio( self.vin.id,'Humble motivated coder')
        profile_list=Profile.objects.all()
        self.assertTrue(len(profile_list)==1)
        new_bio=Profile.objects.all().first()
        self.assertTrue(new_bio.bio=='Humble motivated coder')





