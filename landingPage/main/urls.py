from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('enviarMensagem/', views.enviarMensagem, name='enviarMensagem'),
    # Add other URL patterns here as needed
]