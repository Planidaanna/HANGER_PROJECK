from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from users.models import User
from .models import Message


@login_required
def chat_view(request):
    users = User.objects.exclude(id=request.user.id) # Получаем всех пользователей, кроме текущего
    messages = Message.objects.all().order_by('timestamp') # Получаем все сообщения
    if request.method == 'POST':
        content = request.POST.get('content')
        Message.objects.create(sender=request.user, content=content)
        return redirect('chat') # Перенаправляем на ту же страницу после отправки

    return render(request, 'chat/chat.html', {'users': users, 'messages': messages})
