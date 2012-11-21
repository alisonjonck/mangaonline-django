from django.db import models

class UserSite(models.Model):
    class Meta:
        verbose_name = 'Usuaro do site'
        verbose_name_plural = 'Usuarios do site'
    nome = models.CharField(max_length=60)
    senha = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
