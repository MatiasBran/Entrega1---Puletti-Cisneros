from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField


class MasDatosUsuario(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
    descripcion = RichTextField(null=True)
    link_pagina = models.CharField(max_length=100)
