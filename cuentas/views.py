from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout,login
from django.contrib.auth import authenticate
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        formulario = CustomUserCreationForm(request.POST)
        if formulario.is_valid():
            formulario.save()
            username = formulario.cleaned_data['username']
            password = formulario.cleaned_data['password1']

            user = authenticate(username=username, password=password)
            profile = UserProfile(user=user, role='user')
            profile.save()

            login(request, user)
            return redirect('Inicio')
        data["form"] = formulario
    return render(request, 'registration/register.html', data)



def exit(request):
    logout(request)
    return redirect('login')

def iniciosesion(request):

    if request.method == 'POST':
        usuario = request.POST.get('username')
        clave = request.POST.get('password')

        user = authenticate(request, username= usuario , password= clave)

        if user is not None:
            profile = UserProfile.objects.get(user=user)

            request.session['perfil']= profile.role

            login(request, user)

            return redirect('Inicio')
        else:
            context= {
                'error':'Error intente denuevo'
            }

            return render(request, 'registration/login.html', context)

    return render(request, 'registration/login.html')

