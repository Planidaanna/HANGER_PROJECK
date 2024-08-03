from django.contrib import admin
from collection_fashon.models import *
# Register your models here.
@admin.register(People)
class People_admin(admin.ModelAdmin):
    list_display = ('id', 'title')
    list_display_links = ('id','title')
    list_filter = ('id','title')
    search_fields = ('id', 'title') 
    
@admin.register(Category_people_clothers)
class Category_people_clothers_admin(admin.ModelAdmin):
    list_display = ('id','slug')
    list_display_links = ('id','slug')
    list_filter = ('id','title')
    search_fields = ('id', 'title') 
    
    
    
@admin.register(Sample)
class Sample_admin(admin.ModelAdmin):
    list_display = ('id','slug')
    list_display_links = ('id','slug')
    ist_filter = ('id','title')
    search_fields = ('id', 'title') 