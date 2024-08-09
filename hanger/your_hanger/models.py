from django.db import models
from users.models import User

# Create your models here.
class Category_clothers_users(models.Model):
    name = models.CharField(max_length=300, verbose_name='Название образа')

    class Meta:
        verbose_name = 'Категория одежды'
        verbose_name_plural = 'Категории одежды'
        db_table = 'Categorys_clothers_users'

    def __str__(self):
        return self.name
    
class Clothers_users_load(models.Model):
    image = models.ImageField(upload_to="cloth_images_users", blank=True, null=True, verbose_name='изображение одежды')
    category = models.ForeignKey(Category_clothers_users, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE) 
    
    class Meta:
        verbose_name = 'Одежда пользователей'
        verbose_name_plural = 'Одежда пользователей'
        db_table = 'Clothers_users_load'
    

    def __str__(self):
        return f"{self.category} {self.user}"