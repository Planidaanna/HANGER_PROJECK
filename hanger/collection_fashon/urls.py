from django.urls import path, re_path
from django.conf.urls.static import static
import collection_fashon.views as collection_fashon

# from hanger_home.views import ContactCreateForm
from collection_fashon.views import *
urlpatterns = [
    
    path('', collection_fashon.Fashion_collection.as_view(), name="fashion_collection"),  
    # path('add_to_favorites',collection_fashon. AddToFavoritesView.as_view(), name='add_to_favorites'),
]   