from django.views.generic.list import ListView
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.edit import UpdateView 


from .forms import BusquedaBlog, FormBlog
from .models import Blog


def index(request):
    return render(request, 'index.html')


def about(request):
    return render(request, 'about.html')



class ListadoBlogs(ListView):
    model = Blog
    template_name = 'inicio/listado_blogs.html'
    
    def get_queryset(self):
        titulo = self.request.GET.get('titulo', '')
        if titulo:
            objects_list = self.model.objects.filter(titulo__icontains=titulo)
        else:
            objects_list = self.model.objects.all()
            
        return objects_list
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BusquedaBlog()
        return context 



@login_required
def crear_blog(request):
    print(request.method)
    if request.method == 'POST':
        form = FormBlog(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data
            autor = data.get('autor')
            fecha = data.get('fecha')
            formulario = Blog(titulo=data.get('titulo'),
                              subtitulo=data.get('subtitulo'),
                              contenido=data.get('contenido'),
                              imagen=data.get('imagen'),                             
                              autor=autor if autor else User.username,
                              fecha=fecha if fecha else datetime.now()
                                )
            formulario.save()
            
            return redirect('listado_blogs')                
        else:
            return render(request, 'inicio/crear_blog.html', {'form':form})          
    
    formularios = FormBlog()    
    return render(request, 'inicio/crear_blog.html', {'form':formularios})



class EditarBlog(LoginRequiredMixin, UpdateView):
    model = Blog
    template_name = 'inicio/editar_blog.html'
    success_url = '/listado-blogs/'
    fields = ['titulo', 'subtitulo', 'contenido', 'imagen', 'fecha']



@login_required
def eliminar_blog(request, id):
    blog = Blog.objects.get(id=id) 
    blog.delete()
    return redirect('listado_blogs')  





def mostrar_blog(request, id):
    blog = Blog.objects.get(id=id)
    return render (request, 'inicio/mostrar_blog.html', {'blog':blog})


