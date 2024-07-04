from django.shortcuts import render, redirect
from django.contrib.auth import logout, login, authenticate
from .models import UserProfile
from .forms import CustomUserCreationForm
from django.contrib.auth.models import Group

# Create your views here.
def register(request):
    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(request.POST)
        if user_creation_form.is_valid():
            user = user_creation_form.save()
            UserProfile.objects.create(user=user, role='default_role') 
            nuevo_usuario_group = Group.objects.get(name='Cliente')
            user.groups.add(nuevo_usuario_group)
            login(request, user)
            return redirect('Inicio') 
    else:
        user_creation_form = CustomUserCreationForm()

    return render(request, 'registration/register.html', {'form': user_creation_form})

def exit(request):
    logout(request)
    return redirect('login')

def iniciosesion(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            profile = UserProfile.objects.get(user=user)
            request.session['perfil'] = profile.role

            login(request, user)
            return redirect('Inicio')
        else:
            context= {
                'error':'Error intente denuevo'
            }

            return render(request, 'registration/login.html', context)

    return render(request, 'registration/login.html')

