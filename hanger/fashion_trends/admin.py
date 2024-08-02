from django.contrib import admin

# Register your models here.
from fashion_trends.models import Fashion_post_news

@admin.register(Fashion_post_news)
class Fashion_post_news_admin(admin.ModelAdmin):
    list_display = ('id', 'title','created_date')
    list_display_links = ('id','title')
    list_filter = ('id','title')
    search_fields = ('id', 'title') 
    ordering = ('-created_date',)