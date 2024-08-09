from typing import Any
from django.shortcuts import get_object_or_404, redirect, render
from django.http import JsonResponse
from django.views import View
from django.views.decorators.csrf import csrf_exempt
import json

# Create your views here.
from django.views.generic import TemplateView, ListView

from collection_fashon.models import *
from .forms import FilterForm

class Fashion_collection(ListView):
    model = Sample
    template_name = 'fashion_collection.html'
    context_object_name = 'collections'
    # paginate_by = 6

    def get_queryset(self):
        form = FilterForm(self.request.GET or None)
        samples = Sample.objects.all()

        if form.is_valid():
            if form.cleaned_data['gender']:
                samples = samples.filter(category__people_women_man=form.cleaned_data['gender'])
            if form.cleaned_data['category']:
                samples = samples.filter(category=form.cleaned_data['category'])

        return samples

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = FilterForm(self.request.GET or None)
        return context
from django.views.generic import TemplateView
#Create your views here.


# class Favorites(TemplateView):
#     template_name  = 'favorites.html'
#     extra_context = {
#         'title': 'Главная страница'
#     }

