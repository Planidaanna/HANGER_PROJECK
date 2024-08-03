from django.db import models

# Create your models here.
class People(models.Model):
    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.CharField(max_length=100,  null=True, verbose_name='слаг')

    class Meta:
        db_table = 'People_categorys'
        verbose_name = 'Ж/М'
        verbose_name_plural = 'Категории людей (женщины и мужчины)'

    def __str__(self):
        return self.title

class Category_people_clothers(models.Model):
    title = models.CharField(max_length=300, verbose_name='Название')
    people_women_man = models.ForeignKey(People,  null=True ,blank=True, on_delete=models.CASCADE, verbose_name='мужчина/женщина')
    slug = models.CharField(max_length=100,  null=True, verbose_name='слаг')

    class Meta:
        verbose_name = 'Категория ообраза'
        verbose_name_plural = 'Категории образов'
        db_table = 'Categorys_people_clothers'

    def __str__(self):
        return self.title


class Sample(models.Model):
    title = models.CharField(max_length=150, verbose_name='Название образа')
    image = models.ImageField(upload_to="cloth_images", blank=True, null=True, verbose_name='изображение образа')
    category = models.ForeignKey(Category_people_clothers,  null=True ,blank=True, on_delete=models.CASCADE, verbose_name='категория')
    slug = models.CharField(max_length=100,  null=True, verbose_name='слаг')
    
    class Meta:
        verbose_name = 'Oбраз'
        verbose_name_plural = 'Образы'
        db_table = 'Sample_people_clothers'

    def __repr__(self):
        return self.title