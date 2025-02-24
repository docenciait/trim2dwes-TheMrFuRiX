from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from .forms import CustomUserCreationForm 
from django.contrib.auth.decorators import login_required

def register(request):
    if request.method == 'POST': 
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save() 
            login(request, user)
    else:
        form = CustomUserCreationForm()
    
    return render(request, 'usuarios/registro.html', {'form': form})

def login_view(request):
    if request.method == 'POST': 
        username = request.POST['username'] 
        password = request.POST['password'] 
        
        user = authenticate(request, username=username, password=password) 
        
        if user is not None:
            login(request, user)
            next_url = request.GET.get('next')
            return render(request, 'denuncias/lista_denuncias.html')
    
    return render(request, 'usuarios/login.html')


@login_required 
def logout_view(request):
    logout(request) 
    return redirect('login')
