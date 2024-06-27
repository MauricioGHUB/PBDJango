from django.urls import path,include
from .views import crear

urlpatterns = [
    path('crear/',crear, name='crear'),

]
