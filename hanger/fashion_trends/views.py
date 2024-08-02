from django.shortcuts import render
# from django.views.generic import TemplateView
# Create your views here.

from django.views.generic import ListView
from django.views.generic import DetailView
from .models import Fashion_post_news


class Fashion_news(ListView):
    model = Fashion_post_news
    template_name = 'fashion_trends.html'
    context_object_name = 'news_trend'
    paginate_by = 2

    def get_queryset(self):
        return Fashion_post_news.objects.order_by('-created_date')
    
class Post_news(DetailView):
    model = Fashion_post_news
    template_name = 'post_news.html'
    context_object_name = 'news_trend'
    pk_url_kwargs = 'id'
    