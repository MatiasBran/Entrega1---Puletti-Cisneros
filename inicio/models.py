from django.db import models
from ckeditor.fields import RichTextField



class Blog(models.Model):
    titulo = models.CharField(max_length=50)
    subtitulo = models.CharField(max_length=50)
    contenido = RichTextField(null=True)
    autor = models.CharField(max_length=50)
    imagen = models.ImageField(upload_to='blog', null=True, blank=True) 
    fecha = models.DateField(null=True)
    
    def __str__(self):
        return f'{self.titulo}'  
