from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

urlpatterns = [
    path('accounts/login/', views.login, name='login'),
    path('logout/', LogoutView.as_view(template_name='accounts/logout.html') , name='logout'),
    path('registrarse/', views.registrarse, name='registrarse'),
    path('perfil/', views.perfil , name='perfil'),
    path('editar-perfil/', views.editar_perfil, name='editar_perfil'),
    path('perfil/cambiar-contrasenia/', views.ChangePasswordView.as_view() , name='cambiar_contrasenia'),
    

    ]