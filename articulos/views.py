from django.shortcuts import render


# Create your views here.

def crear(request):
    return render(request,'crud/crear.html')



