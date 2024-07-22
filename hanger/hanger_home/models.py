from django.db import models

# Create your models here.
# Модель "Запрос на связь со стилистом"
class Contact_with_to_a_stylist(models.Model):
    first_name = models.CharField(max_length=30, verbose_name="Имя", default=None)
    surname = models.CharField(max_length=100, verbose_name="Фамилия", default=None)
    patronymic = models.CharField(max_length=100, verbose_name = "Отчество", default=None)
    created_request = models.DateTimeField(auto_now_add=True,verbose_name='Дата отправки запроса на связь')
    phone_number_client = models.CharField(max_length=15, verbose_name='Номер телефона')
    contact_by_phone_number = models.BooleanField(default=False, verbose_name='Связь по номеру телефона')
    contact_by_telegram = models.BooleanField(default=False, verbose_name='Связь по telegram')
    contact_by_vk = models.BooleanField(default=False, verbose_name='Связь по VK')
    contact_by_whatsApp = models.BooleanField(default=False, verbose_name='Связь по whatsApp')
    client_request= models.CharField(max_length=100, default='Просто разобрать свой гардироб', verbose_name='Запрос клиента') 

    class Meta:
        db_table = 'Contact_with_to_a_stylist' 
        verbose_name = 'Запрос на связь со  стилистом'
        verbose_name_plural = 'Запросы'
        
    def __str__(self) -> str:
        return f"Запрос от пользователя {self.first_name} {self.surname} {self.patronymic}"                                 
    