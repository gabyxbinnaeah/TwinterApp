from django import forms
from .models import Image,Profile,Comment 
from django.contrib.auth.models import User

class ImageForm(forms.ModelForm):
    class Meta:

        model=Image
        exclude=['likes','comment','user']


class ProfileFormm(forms.ModelForm):
    class Meta:

        model=Profile
        exclude=['user']

class CommentForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['comment'].widget = forms.TextInput()
        self.fields['comment'].widget.attrs['placeholder'] = 'Add  comment...'
    class Meta:
        model = Comment
        fields = ('comment',)

class UpdateImageFormm(forms.ModelForm):
    class Meta:

        model=Image
        exclude=['likes','comment','user']


class UpdateProfileForm(forms.ModelForm):
    class Meta:

        model=Profile
        exclude=['user']

class UpdateCommentsForm(forms.ModelForm):
    class Meta:

        model=Image
        fields=['comments']

class UpdateUserForm(forms.ModelForm):
    email = forms.EmailField(max_length=255, help_text='Required.Kindly provide a valid email.')
    class Meta:

        model=User
        fields=['email','username'] 

        



