import re
from typing import Any
from django import forms

from hanger_home.models import Contact_with_to_a_stylist

#form "Запрос на связь со стилистом"

class CreateFormsContactWithStylist(forms.ModelForm):
    first_name = forms.CharField(
        label='Имя',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите ваше имя',
            }
        )
    )

    surname = forms.CharField(
        label='Фамилия',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите вашу фамилию',
            }
        )
    )

    patronymic = forms.CharField(
        label='Отчество',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Введите ваше отчество',
            }
        )
    )

    phone_number_client = forms.CharField(
        label='Номер телефона',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Номер телефона',
            }
        )
    )
    
    contact_by_phone_number = forms.BooleanField(
        label='Связаться по номеру телефона',
        required=False,
    )
    
    contact_by_telegram = forms.BooleanField(
        label='Связаться в telegram',
        required=False,
    )
    contact_by_vk = forms.BooleanField(
        label='Связаться в VK',
        required=False,
    )
    
    contact_by_whatsApp = forms.BooleanField(
        label='Связаться в WhatsApp',
        required=False,
    )
    client_request = forms.CharField(
        label='Ваш запрос стилисту',
        widget=forms.TextInput(
            attrs={
                'placeholder': 'Просто разобрать свой гардероб',
            }
        )
    )
    error_css_class = "error"

    class Meta:
        model = Contact_with_to_a_stylist
        fields = '__all__'

    def clean_phone_number_client(self):
        phone_number_client = self.cleaned_data['phone_number_client']
        if not phone_number_client.isdigit():
            raise forms.ValidationError('Номер телефона содержит буквы. ОШИБКА ВВЕДЕНИЯ!')
        
        re_num = re.compile(r'^\d{10}$')
        if re_num.match(phone_number_client):
            return phone_number_client
        raise forms.ValidationError('Проверьте написание номера')
    
    def clean_first_name(self): 
        first_name = self.cleaned_data['first_name']
        if first_name == '':
            raise forms.ValidationError('Заполните поле Имя')
        blok_sumbol = ['<', '>', '=', '!', '@', '#', '$', '&', '^', '*','(', ')', '+', '-', '_', '~', '?']
        for blok in blok_sumbol:
            if blok in first_name:
                raise forms.ValidationError('Проверте заполнения поля Имя! Содержатся недопустимые символы!')
        re_namb = re.compile(r'[0-9]')
        if re_namb.search(first_name):
            raise forms.ValidationError('Проверте заполнения поля Имя! Оно не должно содержать цифр!')
        return first_name
            
    def clean_patronymic(self): 
        patronymic = self.cleaned_data['patronymic']
        if patronymic == '':
            raise forms.ValidationError('Заполните поле Отчество')
        blok_sumbol2 = ['<', '>', '=', '!', '@', '#', '$', '&', '^', '*','(', ')', '+', '-', '_', '~', '?']
        for blok in blok_sumbol2:
            if blok in patronymic:
                raise forms.ValidationError('Проверте заполнения поля Отчество! Содержатся недопустимые символы!')
        re_namb = re.compile(r'[0-9]')
        if re_namb.search(patronymic):
            raise forms.ValidationError('Проверте заполнения поля Отчество! Оно не должно содержать цифр!')
        return patronymic

    def clean_surname(self): 
        surname = self.cleaned_data['surname']
        if surname == '':
            raise forms.ValidationError('Заполните поле Фамилия')
        blok_sumbol3 = ['<', '>', '=', '!', '@', '#', '$', '&', '^', '*','(', ')', '+', '-', '_', '~', '?']
        for blok in blok_sumbol3:
            if blok in surname:
                raise forms.ValidationError('Проверте заполнения поля Фамилия! Содержатся недопустимые символы!')
        re_namb = re.compile(r'[0-9]')
        if re_namb.search(surname):
            raise forms.ValidationError('Проверте заполнения поля Фамилия! Оно не должно содержать цифр!')
        return surname
        
        

   