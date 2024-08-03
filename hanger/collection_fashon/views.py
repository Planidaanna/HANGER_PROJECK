from typing import Any
from django.shortcuts import render
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

# class AddToFavoritesView(View):
#     template_name = 'favorites.html'
#     @csrf_exempt  # Отключаем защиту CSRF для этого метода (не рекомендуется в производственной среде)
#     def post(self, request):
#         try:
#             data = json.loads(request.body)
#             collection_id = data.get('id')

#             # Здесь вы можете добавить код для сохранения коллекции в избранное
#             # Например, добавление в базу данных или в сессию пользователя

#             return JsonResponse({'message': 'Элемент успешно добавлен в избранное!'}, status=200)
#         except Exception as e:
#             return JsonResponse({'error': str(e)}, status=500)    