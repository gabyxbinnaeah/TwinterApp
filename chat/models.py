from django.db import models
from django.contrib.auth.models import User 
import cloudinary
from cloudinary.models import CloudinaryField
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.exceptions import ObjectDoesNotExist
# Create your models here.
class Image(models.Model):
    image = cloudinary.models.CloudinaryField('pics',null=True, blank=True)
    name = models.CharField(max_length=25,blank=True, null=True)
    caption = models.CharField(max_length=40,blank=True, null=True)
    user = models.ForeignKey('Profile', on_delete=models.CASCADE, related_name='images',blank=True, null=True)
    likes= models.IntegerField(default=0)
     

    def save_image(self):
        '''
        Method that saves class image t
        '''
        self.save()

    @classmethod
    def images(cls):
        '''
        Method that returns all image properties
        '''
        images = cls.objects.all()
        return images

    def image_url(self):
        '''
        method that defines image url that connects to our database
        '''
        if self.image and hasattr(self.image, 'url'):
            return self.image.url

    def delete_image(self):
        '''
        method that deletes specified image using image id 
        '''
        self.delete()
       

    @classmethod
    def update_image(cls,old,new):
        '''
        method that updates image
        '''
        cap = Image.objects.filter(caption=old).update(caption=new)
        return cap

    def __str__(self):
       return self.name

    
    


class Profile(models.Model):
    photo = cloudinary.models.CloudinaryField('image',null=True, blank=True)
    bio = models.CharField(max_length=255,blank=True, null=True)
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile',null=True)
    name=models.CharField(max_length=40,blank=True,null=True)


    def save_profile(self):
        '''
         Defines method that saves profile class model
        '''
        self.save()

    @classmethod
    def profile(cls):
        '''
        method that queries the properties of profile class model
        '''
        profiles = cls.objects.all()
        return profiles
        
    def photo_url(self):
        if self.photo and hasattr(self.photo, 'url'):
            return self.photo.url

    @receiver(post_save, sender=User)  
    def create_user_profile(sender, instance, created, **kwargs):
        '''
        method that creates user profile signal
        '''
        try:
            instance.profile.save()

        except ObjectDoesNotExist:
            Profile.objects.create(user=instance)


    @receiver(post_save, sender=User)
    def save_user_profile(sender, instance, **kwargs):
        '''
        method that saves user profile signal
        '''
        instance.profile.save()


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
        return cls.objects.filter(id=id).update(bio=bio) 

    @classmethod
    def search_profile(cls, name):
        '''
        method that filters user profile by name
        '''
        return cls.objects.filter(user__username__icontains=name).all()

    def __str__(self):
        return str(self.name) if self.name else ''

class Follow(models.Model):
    follower = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='following',blank=True, null=True)
    followed = models.ForeignKey(Profile, on_delete=models.CASCADE, related_name='followers',blank=True, null=True)

    def __str__(self):
        return f'{self.follower} Follow'

class Comment(models.Model):
    user = models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='comment')
    photo = models.ForeignKey('Image',on_delete=models.CASCADE,related_name='comment')
    comment=models.TextField()

    class Meta:
        ordering=["-pk"]

    def __str__(self):
        return f'{self.user.name} Image' 

    
   