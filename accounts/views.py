from django.shortcuts import redirect, render
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from django.contrib.auth.views import PasswordChangeView
from accounts.models import MasDatosUsuario
from .forms import MyUserCreationForm, MyUserEditForm 
from django.contrib.auth.decorators import login_required


def login(request):    
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)        
        if form.is_valid():
            username = form.cleaned_data.get('username') 
            password = form.cleaned_data.get('password')             
            user = authenticate(username=username, password=password)            
            if user is not None:
                django_login(request, user)                
                return render(request, 'index.html', {})     
            else:
                return render(request, 'accounts/login.html', {'form': form})          
        else:
            return render(request, 'accounts/login.html', {'form': form})             
    form = AuthenticationForm()            
    return render(request, 'accounts/login.html', {'form': form})



def registrarse(request):
    if request.method == 'POST':
        form = MyUserCreationForm(request.POST)    
        if form.is_valid():
            form.save()

            return render(request, 'index.html', {})          
        else:
            return render(request, 'accounts/registrarse.html', {'form': form})   
    
    form = MyUserCreationForm()
    return render(request, 'accounts/registrarse.html', {'form': form})




def perfil(request):    
    return render(request, 'accounts/perfil.html')



def editar_perfil(request):
    user = request.user
    mas_datos_usuario, _ = MasDatosUsuario.objects.get_or_create(user=user) 
    
    if request.method == 'POST':
        form = MyUserEditForm(request.POST, request.FILES)  
        if form.is_valid():
            data = form.cleaned_data
           
            user.first_name = data.get('first_name') if data.get('first_name') else user.first_name
            user.last_name = data.get('last_name') if data.get('last_name') else user.last_name
            user.email = data.get('email') if data.get('email') else user.email
            mas_datos_usuario.avatar = data.get('avatar') if data.get('avatar') else mas_datos_usuario.avatar 
                   
            mas_datos_usuario.save()  
            user.save()     
                   
            return redirect('perfil')        
        else:
            return render(request, 'accounts/editar_perfil.html', {'form':form})     
        
    form = MyUserEditForm(
        initial={
            'email': user.email, 
            'first_name': user.first_name, 
            'last_name': user.last_name,
            'avatar': mas_datos_usuario.avatar,})
    
    return render(request, 'accounts/editar_perfil.html', {'form':form})



class ChangePasswordView(PasswordChangeView):
    template_name = 'accounts/cambiar_contrasenia.html'
    success_url = '/perfil/'