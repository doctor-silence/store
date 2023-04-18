from django.shortcuts import render, HttpResponseRedirect
from django.contrib import auth
from django.urls import reverse
from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data=request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = auth.authenticate(username=username, password=password) # Проверка на Аутентификацию
            if user:
                auth.login(request, user)      # Проверка наличия юзера в бд
                return HttpResponseRedirect(reverse('index'))  # Переадресация после авторизации
    else:
        form = UserLoginForm()
    context = {'form': form}   #Обращаемся к форме и передаем ее в context
    return render(request, 'users/login.html', context)  #Создаем представление логин


def registration(request):
    if request.method == 'POST':
        form = UserRegistrationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users:login'))
    else:
        form = UserRegistrationForm()
    context = {'form': form}
    return render(request, 'users/registration.html', context) #Создаем представление регистрации

def profile(request):
    context = {'title': 'Store - Профиль'}
    return render(request, 'users/profile.html', context)