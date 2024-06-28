from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout,login
from django.contrib.auth import authenticate
from .models import UserProfile
from django.contrib.auth.models import User

# Create your views here.
def register(request):
    return render(request, 'registration/register.html')



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

