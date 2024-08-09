from django.urls import path

from  your_hanger.views import *

urlpatterns = [
    path('upload/',upload, name='upload'),
    path('my_list/', list, name='my_list'),
]