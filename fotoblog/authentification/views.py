from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.views.generic import View
from authentification import forms
from . import forms
# Create your views here.



def signup_page(request):
    form = forms.SignupForm()
    if request.method == 'POST':
        form = forms.SignupForm(request.POST)
        if form.is_valid():
            user = form.save()
            # auto-login user
            login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    return render(request, 'authentification/signup.html', context={'form': form})



class LoginView(View):
	template_name = 'authentificatio/login.html'
	form_class = forms.LoginForm

	def get(self, request):
		form = self.form_class()
		message = ''
		return render(request,self.template_name, context={'form':form, 'message':message})

	


def logout_user(request):
	logout(request)
	return redirect('login')


def login_page(request):
    form = forms.LoginForm()
    message = ''
    if request.method == 'POST':
        form = forms.LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(
                username=form.cleaned_data['username'],
                password=form.cleaned_data['password'],
            )
            if user is not None:
                login(request, user)
                return redirect('home')
            
        message = 'Login failed!'
    return render(
        request, 'authentification/login.html', context={'form': form, 'message': message})


