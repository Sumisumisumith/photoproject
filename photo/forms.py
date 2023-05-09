from django.forms import ModelForm
from .models import PhotoPost
from django import forms

class PhotoPostForm(ModelForm):
    class Meta:
        model = PhotoPost
        fields = ['category','title','comment','image1', 'image2', 'image3', 'image4', 'image5','image6','image7','image8','image9',]

class SearchForm(forms.Form):
    query = forms.CharField(label='検索するキーワード', max_length=100)
