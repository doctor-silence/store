from django.urls import reverse_lazy

from django.views.generic.edit import CreateView, UpdateView
from django.contrib.auth.views import LoginView
from django.contrib.messages.views import SuccessMessageMixin

from users.models import User
from users.forms import UserLoginForm, UserRegistrationForm, UserProfileForm
from products.models import Basket


class UserLoginView(LoginView):
    template_name = 'users/login.html'
    form_class = UserLoginForm



class UserRegistrationView(CreateView):
    model = User
    form_class = UserRegistrationForm
    template_name = 'users/registration.html'
    success_url = reverse_lazy('users:login')
    
    def get_context_data(self, **kwargs):              # Формирование тайтла
        context = super(UserRegistrationView, self).get_context_data()
        context['title'] = 'Store - Регистрация'
        return context


class UserProfileView(UpdateView):
    model = User
    form_class = UserProfileForm
    template_name = 'users/profile.html'

    def get_success_url(self):
        return reverse_lazy('users:profile', args=(self.object.id,))   # Переброс после обновления данных

    def get_context_data(self, **kwargs):              # Формирование тайтла
        context = super(UserProfileView, self).get_context_data()
        context['title'] = 'Store - Личный кабинет'
        context['baskets'] = Basket.objects.filter(user=self.object)
        return context



#def login(request):
#    if request.method == 'POST':
#        form = UserLoginForm(data=request.POST)
#        if form.is_valid():
 #           username = request.POST['username']
 #           password = request.POST['password']
#            user = auth.authenticate(username=username, password=password) # Проверка на Аутентификацию
#            if user:
#                auth.login(request, user)      # Проверка наличия юзера в бд
#                return HttpResponseRedirect(reverse('index'))  # Переадресация после авторизации
 #   else:
 #       form = UserLoginForm()
 #   context = {'form': form}   #Обращаемся к форме и передаем ее в context
 #   return render(request, 'users/login.html', context)  #Создаем представление логин


#def registration(request):
#    if request.method == 'POST':
#        form = UserRegistrationForm(data=request.POST)
#        if form.is_valid():
#            form.save()
#            messages.success(request, 'Вы успешно зарегистрированы!')  # Добавляем уведомление messages.success
#            return HttpResponseRedirect(reverse('users:login'))
#        else:
#            print(form.errors)
#    else:
#        form = UserRegistrationForm()
#    context = {'form': form}
#    return render(request, 'users/registration.html', context) #Создаем представление регистрации



#@login_required
#def profile(request):
#    if request.method == 'POST':
#        form = UserProfileForm(instance=request.user, data=request.POST, files=request.FILES)
#        if form.is_valid():
#            form.save()
#            messages.success(request, 'Изменения прошли успешно')
#            return HttpResponseRedirect(reverse('users:profile'))
#    else:
#        form = UserProfileForm(instance=request.user)
#
#    context = {
#        'title': 'Store - Профиль',
#        'form': form,
#        'baskets': Basket.objects.filter(user=request.user),
#    }
#    return render(request, 'users/profile.html', context)
