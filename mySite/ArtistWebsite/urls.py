from django.urls import path, include
from . import views

urlpatterns = [
    path('home/', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('products/', views.products, name='products'),
    path('contact/', views.contact, name='contact'),
    
]
