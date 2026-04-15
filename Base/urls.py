from django.urls import path
from . import views

urlpatterns = [
    path('', views.contact, name='home'),   # homepage
    path('about', views.about, name='about'),  # about page
]