from django.urls import path
from . import views
app_name = 'contacto'

urlpatterns = [
    path('contact/', views.contact, name= 'contact')
]
