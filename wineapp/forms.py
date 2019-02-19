from django import forms
from .models import Wine

class  WineForm(forms.ModelForm):
    class Meta:
        model = Wine
        fields = ['country', 'description', 'designation', 'points', 'price', 'province', 'region_1', 'region_2', 'variety', 'winery']
