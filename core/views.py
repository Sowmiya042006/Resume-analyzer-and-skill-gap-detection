from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.urls import reverse
from analyzer.models import Resume

def home(request):
    return render(request, 'index.html')

@login_required
def dashboard(request):
    resumes = Resume.objects.filter(user=request.user).order_by('-uploaded_at')
    
    avg_score = 0
    if resumes.exists():
        total_score = sum(r.match_score for r in resumes)
        avg_score = int(total_score / resumes.count())

    context = {
        'resumes': resumes,
        'total_analyzed': resumes.count(),
        'avg_score': avg_score
    }
    return render(request, 'dashboard.html', context)

from .forms import EmailSignUpForm, EmailLoginForm

def signup_view(request):
    if request.method == 'POST':
        form = EmailSignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user, backend='django.contrib.auth.backends.ModelBackend')
            return redirect('dashboard')
    else:
        form = EmailSignUpForm()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = EmailLoginForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('dashboard')
    else:
        form = EmailLoginForm()
    return render(request, 'login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect('home')
