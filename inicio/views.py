from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required
def vistaIndex(request):
    return render(request,'inicio/index.html')

# Create your views here.
def vistaNosotros(request):
    return render(request,'inicio/nosotro.html')