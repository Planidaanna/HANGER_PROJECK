from django.conf import settings
from django.urls import path, re_path
from django.conf.urls.static import static

import hanger_home.views as hanger_home

from hanger_home.views import ContactCreateForm
from hanger_home.views import *


urlpatterns = [
    
    path('', hanger_home.Home.as_view(), name="hanger_home"),
    path('contact_form/', ContactCreateForm.as_view(), name="contact_form"),
    path('user_agreement/', UserAgreement.as_view(), name="user_agreement"),
    path('legal_information/', LegalInformation.as_view(), name="legal_information"),
    path('privacy_policy/', PrivacyPolicy.as_view(), name="privacy_policy"),     
]   
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)