from django import forms
from ckeditor.fields import RichTextFormField



class FormBlog(forms.Form):
    titulo = forms.CharField(max_length=50)
    subtitulo = forms.CharField(max_length=50)
    contenido = RichTextFormField()
    autor = forms.CharField(max_length=50, required=False)
    imagen = forms.ImageField()
    fecha = forms.DateField(required=False)
   
    
    
class BusquedaBlog(forms.Form):
    titulo = forms.CharField(max_length=50, required=False)