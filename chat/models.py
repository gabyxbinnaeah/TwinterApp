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
        self.save()

    def delete_image(self):
        self.delete(self) 

    


class Profile(models.Model):
    profile_photo=models.ImageField(upload_to='pics',blank=True)
    bio= models.CharField(max_length=1000,blank=True,null=True)
