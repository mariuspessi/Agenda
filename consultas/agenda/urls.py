from django.urls import path
from .views import home, Cliente


urlpatterns = [
    path('', home),

    path('clientes', Cliente),
    
]