from django import forms
from .models import Image,Profile
from django.conf.auth.models import User

class ImageFormm(forms.ModelForm):
    class Meta:

        model=Image
        exclude=['likes','comments','user']


class ProfileFormm(forms.ModelForm):
    class Meta:

        model=Profile
        exclude=['user']

class UpdateImageFormm(forms.ModelForm):
    class Meta:

        model=Image
        exclude=['likes','comments','user']


class UpdateProfileForm(forms.ModelForm):
    class Meta:

        model=Profile
        exclude=['user']

class UpdateCommentsForm(forms.ModelForm):
    class Meta:

        model=Image
        fields=['comments']

class UpdateUserForm(forms.ModelForm):
    class Meta:

        model=User
        fields=['name','email','username']



