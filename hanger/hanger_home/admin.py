from django.contrib import admin

from hanger_home.models import Contact_with_to_a_stylist

# Register your models here.
@admin.register(Contact_with_to_a_stylist)
class Contact_with_to_a_stylist_admin(admin.ModelAdmin):
    list_display = ('first_name', 'surname', 'patronymic', 'created_request','client_request')
    list_display_links = ('first_name', 'surname')