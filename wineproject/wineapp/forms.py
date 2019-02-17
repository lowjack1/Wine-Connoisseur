from django import forms
from .models import Contact

class  ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ('sno', 'country', 'description', 'designaion', 'points', 'price', 'province', 'region_1', 'region_2', 'variety', 'winery')
