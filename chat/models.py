from django.db import models

# Create your models here.
class Image(models.Model):
    image= models.ImageField(upload_to='pics',blank=True)
    image_name = models.CharField(max_length=60,blank=True,null=True)
    image_captions= models.CharField(max_length=60,blank=True,null=True)
    profile=models.ForeignKey('Profile',on_delete=models.CASCADE,null=True)
    likes= models.IntegerField(default=0)
    comments=models.CharField(max_length=500) 

    def __str__(self):
        return self.image_name

    def save_image(self):
        '''
        Method that saves class image t
        '''
        self.save()

    def delete_image(self):
        '''
        method that deletes specified image using image id 
        '''
        Image.objects. filter(id=self.id).delete()

    @classmethod
    def update_caption(cls,id,image_caption):
        '''
        Method that update image caption 
        '''
        return cls.objects.filter(id=id).update(image_caption=image_caption)


    


class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='pics',blank=True)
    bio= models.CharField(max_length=1000,blank=True,null=True)

    def __str__(self):
        return self.bio

    def save_profile(self):
        '''
         Defines method that saves profile class model
        '''
        self.save()

    def delete_profile(self):
        '''
         Method that deletes profile
        '''
        Profile.objects.filter(id=self.id).delete()


    @classmethod
    def update_profile_bio(cls,id,bio):
        '''
         Method that updates user profile bio
        '''
        return cls.objects.filter(id=id).upadate(bio=bio) 
    
