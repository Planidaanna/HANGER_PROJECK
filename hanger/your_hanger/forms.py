from django import forms
from .models import Category_clothers_users, Clothers_users_load 

class ItemForm(forms.ModelForm):
    
    category = forms.ModelChoiceField(
        queryset=Category_clothers_users.objects.all(), 
        required=False, 
        label="Стили образов" 
    )
    class Meta:
        model = Clothers_users_load
        fields = ('image', 'category')