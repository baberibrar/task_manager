from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from tasks.forms import UserRegisterForm
from django.contrib.auth.views import LogoutView

class CustomLogoutView(LogoutView):
    http_method_names = ['get', 'post', 'head', 'options']


def register(request):
    if request.user.is_authenticated:
        return redirect('task-list')
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('task-list')
    else:
        form = UserRegisterForm()
    return render(request, 'tasks/register.html', {'form': form})



