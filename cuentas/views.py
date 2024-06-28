from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth import logout,login,authenticate
from .models import UserProfile
from django.contrib.auth.models import User
from .forms import CustomUserCreationForm

# Create your views here.
def register(request):
    data = {
        'form': CustomUserCreationForm()
    }

    if request.method == 'POST':
        user_creation_form = CustomUserCreationForm(data=request.POST)
        if user_creation_form.is_valid():
            user_creation_form.save()

            user = authenticate(username=user_creation_form.cleaned_data['username'], password=user_creation_form.cleaned_data['password1'])
            return redirect('login')
        
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

