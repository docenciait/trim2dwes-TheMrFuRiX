from django.urls import path, include
from . import views

urlpatterns = [
    path('registro/', views.register, name='registro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),  
]