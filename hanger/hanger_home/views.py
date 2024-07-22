from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from hanger_home.forms import CreateFormsContactWithStylist
from hanger_home.models import Contact_with_to_a_stylist
from hanger_home.forms import *
from django.views.generic import TemplateView
#Create your views here.


class Home(TemplateView):
    template_name  = 'home.html'
    extra_context = {
        'title': 'Главная страница'
    }


class ContactCreateForm(CreateView):
    model = Contact_with_to_a_stylist
    form_class = CreateFormsContactWithStylist
    template_name = 'base.html'
    extra_context = {'title': "Форма связи с клиентом"}
    success_url = ('hanger')

    def form_invalid(self, form):
        return super().form_invalid(form) 

def success(request):
   return HttpResponse('Форма отправлена!')


def index(request):
    return render(request, 'base.html')
