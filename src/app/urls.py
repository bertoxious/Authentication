from django.urls import path
from . import views 
from django.contrib.auth import views as avs

urlpatterns = [
    path('register/', views.Register, name='register'),
    path('view/', views.View, name='view'),
     path('details/<int:id>', views.Detail, name='detail'),
    path('delete/<int:id>/', views.Delete, name='deleted'),
    path('login/', avs.LoginView.as_view(template_name='app/login.html'), name='login'),
    path('logout/', avs.LogoutView.as_view(template_name='app/logout.html'), name='logout'),
]
