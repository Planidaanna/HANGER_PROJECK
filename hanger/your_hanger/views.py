from pyexpat.errors import messages
from django.http import HttpResponseNotFound, HttpResponseRedirect
from django.shortcuts import get_object_or_404, redirect, render

from your_hanger.forms import*
from your_hanger.models import *
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def upload(request):
    """
    Страница загрузки фото и добавления элемента в категорию (только для авторизованных пользователей).
    """
    if request.method == 'POST':
        form = ItemForm(request.POST, request.FILES)
        if form.is_valid():
            item = form.save(commit=False)
            category_id = request.POST.get('category') 
            if category_id:
                try:
                    item.category = Category_clothers_users.objects.get(pk=category_id) 
                    item.user = request.user
                    item.save()
                    return redirect('upload')
                except Category_clothers_users.DoesNotExist:
                    messages.error(request, 'Категория не найдена.')
            else:
                messages.error(request, 'Выберите категорию.')
    else:
        form = ItemForm()
        categories = Category_clothers_users.objects.all()
        context = {
        'form': form,
        'categories': categories,
        }
    return render(request, 'upload_user_clothers.html', context)

@login_required
def list(request, category_id=None):
    """
    Отображение списка элементов в категории.
    """
    category = None
    items = Clothers_users_load.objects.filter(user=request.user)
    if category_id:
        category = get_object_or_404(Category_clothers_users, pk=category_id)
        items = items.filter(category=category)
    context = {
        'category': category,
        'items': items,
    }
    return render(request, 'user_clothers_list.html', context)
@login_required
def delete_item(request, item_id):
    if request.method == "POST": 
        Clothers_users_load.objects.get(id=item_id).delete()
    else:
        messages.error(request, "Не удалось удалить запись ")
    return redirect(request.META.get('HTTP_REFERER', '/')) 
