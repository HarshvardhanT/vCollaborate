from django.shortcuts import render, redirect
from .forms import SignUpForm
from django.contrib.auth import login
from django.contrib.auth import logout
from django.http import HttpResponseNotAllowed

def startpage(request):
    return render(request, "index.html")

def project(request):
    return render(request, "project.html")

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)

        if form.is_valid():
            user = form.save()

            login(request, user)

            return redirect('project')
    else:
        form = SignUpForm()
    
    return render(request, 'account/signup.html', {'form': form})

def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('homepage')  # or any other page you want to redirect to after logout
    return HttpResponseNotAllowed(['POST'])