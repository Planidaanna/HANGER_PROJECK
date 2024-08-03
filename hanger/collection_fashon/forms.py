from django import forms
from .models import People, Category_people_clothers

class FilterForm(forms.Form):
    gender = forms.ModelChoiceField(
        queryset=People.objects.all(), 
        required=False, 
        label="Женщины/мужчины"
    )
    category = forms.ModelChoiceField(
        queryset=Category_people_clothers.objects.all(), 
        required=False, 
        label="Стили образов" 
    )
    
    