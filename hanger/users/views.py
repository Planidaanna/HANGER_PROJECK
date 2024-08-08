
# Create your views here.
from django.conf import settings
from django.shortcuts import render
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from .forms import LoginUserForm, ProfileUserForm
from django.views.generic.edit import FormView, CreateView, UpdateView
from .forms import RegisterUserForm, UserPasswordChangeForm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import get_user_model
from django.contrib.auth.views import PasswordChangeView, PasswordChangeDoneView
class LoginUser(LoginView):
    form_class = LoginUserForm
    template_name = 'login.html'
    extra_context = {'form': form_class}

    def get_success_url(self):
        return reverse_lazy('hanger_home')
    
class LogoutUser(LogoutView):
    next_page = reverse_lazy('hanger_home')
    
class RegisterUser(CreateView):
    form_class = RegisterUserForm
    template_name = 'register.html'
    extra_context = {'title': "Регистрация"}
    success_url = reverse_lazy('login')
    
class ProfileUser(LoginRequiredMixin, UpdateView):
    model = get_user_model()
    form_class = ProfileUserForm  
    template_name = 'profile.html' 
    extra_context = {'title': "Профиль пользователя", 
                     'default_image': settings.DEFAULT_USER_IMAGE}

    def get_success_url(self):
        return reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user

class UserPasswordChange(PasswordChangeView):
    form_class = UserPasswordChangeForm
    template_name = 'password_change_form.html'
    extra_context = {'title': "Изменение пароля"}

    def get_success_url(self):
        return reverse_lazy('password_change_done')