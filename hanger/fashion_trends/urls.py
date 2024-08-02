from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static
import fashion_trends.views as fashion_trends

# from hanger_home.views import ContactCreateForm
from fashion_trends.views import *
urlpatterns = [
    
    path('', fashion_trends.Fashion_news.as_view(), name="fashion_news"),  
    path("<int:pk>/", fashion_trends.Post_news.as_view(), name="post_news"),
]   