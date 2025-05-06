from django.shortcuts import render, redirect
from .forms import SignUpForm
from .models import User
from django.contrib import messages
from .forms import LoginForm
from .models import User

def login_required(view_func):
    def wrapper(request, *args, **kwargs):
        if not request.session.get('user_id'):
            return redirect('login')
        return view_func(request, *args, **kwargs)
    return wrapper

def register(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.password = form.cleaned_data['password1'] 
            user.save()
            messages.success(request, 'You have successfully registered.')
            return redirect('login')  
    else:
        form = SignUpForm()
    return render(request, 'users/register.html', {'form': form})
def login_view(request):
    error = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            uname = form.cleaned_data['username']
            pw = form.cleaned_data['password']
            try:
                user = User.objects.get(username=uname, password=pw)
                request.session['user_id'] = user.id
                print("Login successful, redirecting...")
                messages.success(request, 'Login successful.')
                return redirect('books.studentlist')
            except User.DoesNotExist:
                messages.error(request, 'Invalid username or password.')
    else:
        form = LoginForm()
    return render(request, 'users/login.html', {'form': form, 'error': error})

from django.contrib.auth import logout
def logoutUser(request):
    logout(request)
    messages.info(request, 'You have been logged out.')

    return redirect('/')