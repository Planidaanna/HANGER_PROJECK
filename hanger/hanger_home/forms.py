import re
from typing import Any
from django import forms

from hanger_home.models import Contact_with_to_a_stylist

#form "Запрос на связь со стилистом"
class CreateFormsContactWithStylist(forms.ModelForm):
    first_name = forms.CharField(
        label= 'Имя',
        widget= forms.TextInput (
            attrs= {
            'placeholder': 'Введите ваше имя',
            }
        )
    )
    
    surname = forms.CharField(
        label= 'Фамилия',
        widget= forms.TextInput(
            attrs= {
            'placeholder': 'Введите ваше отчество',
            }
        )
    )
    
    patronymic = forms.CharField(
        label= 'Отчество',
        widget= forms.TextInput(
            attrs= {
            'placeholder': 'Введите вашу фамилию',
            }
        )
    )
    
    
    phone_number_client = forms.CharField(
        label= 'Номер телефона',
        widget= forms.TextInput(
            attrs={
                'placeholder': 'Номер телефона',
                
            }
        ),
        
    )
    error_css_class = "error"
    
    class Meta:
        model = Contact_with_to_a_stylist
        fields = '__all__' 
    
    def clean_phone_number(self):
        phone_number_client = self.cleaned_data['phone_number_client']
        if not phone_number_client.isdigit():
            raise forms.ValidationError('Номер телефона содержит буквы.ОШИБКА ВВЕДЕНИЯ!')
        re_num = re.compile( r'^\d{10}$')
        if re_num.match(phone_number_client):  # Изменено условие
            return phone_number_client
        raise forms.ValidationError('Проверте написание номера')

    def clean_first_name(self): 
        first_name = self.cleaned_data['first_name']
        if not first_name:  # Изменено условие
            raise forms.ValidationError('Заполните поле Имя')
        return first_name

    def clean_patronymic(self): 
        patronymic = self.cleaned_data['patronymic']
        if not patronymic:  # Изменено условие
            raise forms.ValidationError('Заполните поле Отчество')
        return patronymic

    def clean_surname(self): 
        surname = self.cleaned_data['surname']
        if not surname:  # Изменено условие
            raise forms.ValidationError('Заполните поле Фамилия')
        return surname

    
    
    # def clean_phone_number(self):
    #     phone_number_client = self.cleaned_data['phone_number_client']
    #     if not phone_number_client.isdigit():
    #         raise forms.ValidationError('Номер телефона содержит буквы.ОШИБКА ВВЕДЕНИЯ!')
    #     re_num = re.compile( r'^\d{10}$')
    #     if not re_num.match(phone_number_client):
    #         raise forms.ValidationError('Проверте написание номера')
    #     return phone_number_client
    
    # def clean_first_name(self): 
    #     first_name= self.cleaned_data['first_name']
    #     if not first_name != '':
    #         raise forms.ValidationError('Заполните поле Имя')
    #     return first_name
    
    # def clean_patronymic(self): 
    #     patronymic = self.cleaned_data['patronymic']
    #     if not patronymic != '':
    #         raise forms.ValidationError('Заполните поле Отчество')
    #     return patronymic
    
    # def clean_surname(self): 
    #     surname = self.cleaned_data['surname']
    #     if not surname != '':
    #         raise forms.ValidationError('Заполните поле Фамилия')
    #     return surname
    
   
    # contact_by_phone_number  = forms.CharField(
    #     widget= forms.ChoiceField(
    #         choices=[
    #             ("0", 'False'),
    #             ("1", 'True'),
    #         ],
    #     )
    # )
    # contact_by_telegram  = forms.CharField(
    #     widget= forms.ChoiceField(
    #         choices=[
    #             ("0", 'False'),
    #             ("1", 'True'),
    #         ],
    #     )
    # )
    
    # contact_by_vk  = forms.CharField(
    #     widget= forms.ChoiceField(
    #         choices=[
    #             ("0", 'False'),
    #             ("1", 'True'),
    #         ],
    #     )
    # )
    
    # contact_by_WhatsApp = forms.CharField(
    #     widget= forms.ChoiceField(
    #         choices=[
    #             ("0", 'False'),
    #             ("1", 'True'),
    #         ],
    #     )
    # )
    
