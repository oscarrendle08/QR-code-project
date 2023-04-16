from django.urls import path

from .views import home, about, qr_generation, analytics

urlpatterns = [
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('qr-generation/', qr_generation, name='qr_generation'),
    path('analytics/', analytics, name='analytics'),
] 

# mywebsite/urls.py
