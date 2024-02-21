from django.urls import path
from .views import home, pacientes


urlpatterns = [
    path('', home),

    path('pacientes', pacientes),
    
]