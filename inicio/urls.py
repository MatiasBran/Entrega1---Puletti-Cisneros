from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('about/', views.about, name='about'),   
    path('listado-blogs/', views.ListadoBlogs.as_view() , name='listado_blogs'),  
    path('crear-blog/', views.crear_blog, name='crear_blog'),
    path('eliminar-blog/<int:id>', views.eliminar_blog, name='eliminar_blog'),
    path('editar-blog/<int:pk>', views.EditarBlog.as_view() , name='editar_blog'),    
    path('mostrar-blog/<int:id>', views.mostrar_blog, name='mostrar_blog'),    
]