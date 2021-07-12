from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class Image(models.Model):
    image= models.ImageField(upload_to='pics',blank=True)
    image_name= models.CharField(max_length=60,blank=True,null=True)
    image_captions= models.CharField(max_length=60,blank=True,null=True)
    user=models.ForeignKey('Profile',on_delete=models.CASCADE,null=True,blank=True)
    likes= models.IntegerField(default=0)
    comments=models.CharField(max_length=500 ,blank=True,null=True) 

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

    @classmethod
    def image_details(cls):
        images_list=cls.objects.all()
        return images_list

    
    


class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='pics',blank=True)
    bio= models.TextField(max_length=1000,blank=True,null=True)
    user= models.OneToOneField(User,related_name="profile",null=True,on_delete=models.CASCADE) 


    def __str__(self):
        return self.bio

    def save_profile(self):
        '''
         Defines method that saves profile class model
        '''
        self.save()
    @classmethod
    def profile_details(cls):
        details_container=cls.objects.all()
        return details_container

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



class Follow(models.Model):
    follower=models.ForeignKey('Profile',on_delete=models.CASCADE,related_name='follower', null=True,blank=True)
    following=models.ForeignKey('Profile',related_name='following',on_delete=models.CASCADE)

    def __str__(self):
        return self.follower

# class Comment(models.Model):
#     user=model.ForeignKey('Profile',related_name='comment',on_delete=CASCADE)
#     comment=models.TextField()
#     photo = models.ForeignKey('Image',related_name='comments',  on_delete=models.CASCADE)

#     class Meta:
#         ordering=["-pk"]

#     def __str__(self):
#         return f'{self.user.name} Image' 

    
   