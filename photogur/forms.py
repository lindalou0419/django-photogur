from django.forms import ModelForm
from photogur.models import Comment, Picture

class PictureForm(ModelForm):
  class Meta:
    model = Picture
    fields = ['title', 'artist', 'url']