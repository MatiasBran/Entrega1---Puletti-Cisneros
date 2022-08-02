from django.db import models
from django.contrib.auth.models import User



class MasDatosUsuario(models.Model):    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatar', null=True, blank=True)
