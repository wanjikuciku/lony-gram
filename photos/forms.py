from django import forms
from .models import Image,Profile
from pyuploadcare.dj.forms import ImageField


class ImageForm(forms.ModelForm):
    image_url = ImageField(label='Picture')
    class Meta:
        model = Image
        fields = ("image_url","name","caption")

class ProfileForm(forms.Form):
    bio = forms.CharField(label = "Bio")
    pic = ImageField(label = "Pic")