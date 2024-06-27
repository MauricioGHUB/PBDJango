from django.shortcuts import render

def vistaIndex(request):
    return render(request,'inicio/index.html')

# Create your views here.
def vistaNosotros(request):
    return render(request,'inicio/nosotro.html')