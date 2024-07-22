from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static

import hanger_home.views as hanger_home

from hanger_home.views import ContactCreateForm
from hanger_home.views import *


urlpatterns = [
    # path('', ContactCreateForm.as_view() ),
    path('', hanger_home.Home.as_view(), name="hanger_home"),
    path('index/', hanger_home.index)
    
    
]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)