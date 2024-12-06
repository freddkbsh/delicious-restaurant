from django import forms
from restaurantApp.models import Table1, ImageModel


class Table1Form(forms.ModelForm):
    class Meta:
        model=Table1
        fields= '__all__'

class ImageUploadForm(forms.ModelForm):
    class Meta:
        model = ImageModel
        fields = '__all__'