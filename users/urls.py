
from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.login_user, name='login_user'),
    path('register/', views.register, name='register'),
    path('users/', views.list_users, name='list_users'),
    path('users/edit/<int:pk>', views.edit_user, name='edit_user'),
    path('users/delete/<int:pk>', views.delete_user, name='delete_user'),
    path('perfil/', views.edit_perfil, name='edit_perfil'),
    path('users/add', views.user_admin, name='user_admin'),
    
    path('logout/', views.exit, name='logout_user'),  # Logout user
]

handler403 = 'users.views.error_403'