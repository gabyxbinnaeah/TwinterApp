from django.db import models

# Create your models here.
class Image(models.Model):
    image= models.ImageField(upload_to='pics',blank=True)
    image_captions= models.CharField(max_length=60,blank=True,null=True)
    profile= models.ForeignKey(Profile,on_delete=models.CASCADE)
    likes= models.IntegerField(default=0)
    comments=models.CharField(max_length=500)
