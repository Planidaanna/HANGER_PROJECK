from django.db import models

# Create your models here.

class Fashion_post_news(models.Model):
    id = models.AutoField(primary_key=True,verbose_name='id новости(публикации)')
    title = models.CharField(max_length=100,verbose_name='Заголовок новости')
    title_text = models.CharField(max_length=300,verbose_name='Подзаголовок')
    text = models.TextField(max_length=5000, verbose_name='текст/содержание')
    image = models.ImageField(upload_to="post_news_images", blank=True, null=True, verbose_name='изображение')
    created_date = models.DateTimeField(auto_now_add=True,verbose_name='Дата добавления новости в базу')
    
    class Meta:
        db_table = 'Fashion_post_news'
        verbose_name = 'Новостные посты о модных тенденциях'
        verbose_name_plural = 'Новости мира моды'
        
    def __str__(self):
        return f"Пост №{self.id} - {self.title}"