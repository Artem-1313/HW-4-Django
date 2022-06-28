from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import FormView
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm
from .forms import NewUserRegistrationForm
# Create your views here.

class LoginClass(FormView):
    form_class = AuthenticationForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        user = authenticate(username=self.request.POST['username'], password=self.request.POST['password'])
        login(self.request, user)
        return super(LoginClass, self).form_valid(form)

class LogoutClass(LoginRequiredMixin, LogoutView):

    redirect_field_name = 'index'
    template_name = "accounts/logout.html"


class RegistrationClass(FormView):
    form_class = NewUserRegistrationForm
    success_url = reverse_lazy('index')
    template_name = 'accounts/registration.html'

    def form_valid(self, form):
        form.save()
        return super(RegistrationClass, self).form_valid(form)

def registration(request):
    if request.method == "POST":
        form=NewUserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form=NewUserRegistrationForm()
    return render(request, 'accounts/registration.html', {'form': form})